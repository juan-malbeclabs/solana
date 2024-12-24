### README for `solana.ipynb`

#### Solana Validators and Gossip Data Analysis

This Jupyter Notebook downloads the list of Solana validators and gossip data, cross-references it with geographical information from ipinfo.io, and exports the combined data to an Excel file.

#### Workflow:
1. Download Solana gossip data using the Solana CLI.
2. Download Solana validators data using the Solana CLI.
3. Cross-reference the gossip data with the validators data.
4. Filter the combined data for validators with an activated stake greater than 0.
5. Retrieve geographical information for each IP address from ipinfo.io.
6. Combine the geographical information with the filtered data.
7. Export the final combined data to an Excel file.

#### Execution Instructions:
1. Ensure you have the Solana CLI installed and configured on your machine.
2. Install the required Python packages:
   ```bash
   pip install pandas requests maxminddb
   ```
3. Set up an IPinfo.io account and obtain your API token.
4. Clone the repository and navigate to the directory containing the Jupyter Notebook.
5. Open the `solana.ipynb` file with Jupyter Notebook:
   ```bash
   jupyter notebook solana.ipynb
   ```
6. Execute the cells in the notebook sequentially to perform the analysis and export the data to an Excel file.

#### Prerequisites:
- Python 3.x
- Solana CLI
- Jupyter Notebook
- Required Python packages (`pandas`, `requests`, `maxminddb`)
- IPinfo.io API token

#### Note:
- Ensure the Solana CLI is properly configured and accessible in your environment.
- Replace the placeholder IPinfo.io token in the notebook with your actual token.

This notebook helps in analyzing Solana validators and gossip data, providing insights into their geographical distribution and stake information.
