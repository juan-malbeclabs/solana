import subprocess, json, pandas as pd, os, requests

def get_solana_gossip():
    solana_cli = os.path.expanduser('~/.local/share/solana/install/active_release/bin/solana')
    result = subprocess.run([solana_cli, 'gossip', '--output', 'json'], capture_output=True)
    if result.stderr:
        raise Exception
    return json.loads(result.stdout)

def get_solana_validators():
    solana_cli = os.path.expanduser('~/.local/share/solana/install/active_release/bin/solana')
    result = subprocess.run([solana_cli, 'validators', '--output', 'json'], capture_output=True)
    if result.stderr:
        raise Exception
    return json.loads(result.stdout)

gossip = get_solana_gossip()
validators = get_solana_validators()

# Create a dictionary for quick access to validators by their identityPubkey
validators_dict = {validator['identityPubkey']: validator for validator in validators['validators']}

# Create a new array combining the gossip and validators information
combined_data = []
for node in gossip:
    pubkey = node['identityPubkey']
    if pubkey in validators_dict:
        combined_entry = {**node, **validators_dict[pubkey]}
        combined_data.append(combined_entry)

for entry in combined_data:
    if 'activatedStake' in entry:
        entry['activatedStake'] = entry['activatedStake'] / 1_000_000_000

# Function to get information from IPinfo.io
def get_ipinfo(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"
    response = requests.get(url)
    return response.json()

# IPinfo.io token
token = "528509095bd574"

# Filter the combined data for those with activatedStake > 0
filtered_data = [entry for entry in combined_data if entry.get('activatedStake', 0) > 0]

# Get information from IPinfo.io and combine it with the filtered data
for entry in filtered_data:
    ip_info = get_ipinfo(entry['ipAddress'], token)
    entry.update(ip_info)

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Flatten each entry in the filtered_data array
flattened_data = [flatten_dict(entry) for entry in filtered_data]

# Convert the flattened data to a DataFrame
df_flattened = pd.DataFrame(flattened_data)

# Export the DataFrame to an Excel file
df_flattened.to_excel('validators.xlsx', index=False)
