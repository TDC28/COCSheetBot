python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
echo '{"Players": {}}' >>playersList.json
echo 'API_KEY=[Your COC api key goes here]' >>.env
echo 'TOKEN=[The token required to use the bot goes here]' >>.env
echo 'Installation was successful, copy Backup.xlsx into src and rename it. When using the !load_main command on discord you will use this filename'
echo 'Open the .env file for final instructions'
echo 'Once setup is finished, to run the but run the following from root of project:'
echo 'source .venv/bin/activate'
echo 'python src/main.py'
