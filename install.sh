python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
echo '{"Players": {}}' >playersList.json
echo 'API_KEY=[Your COC api key goes here]' >.env
echo 'TOKEN=[The token required to use the bot goes here]' >>.env
deactivate
rm install.sh

printf '\n\n🎉 Installation was successful, copy Template.xlsx into src and rename it. When using the !load_main command on discord you will use this filename (default: CWL2024.xlsx).\n'
printf '  Open the .env file for final instructions\n'
printf '  Once setup is finished, to start the bot, run the following from root of project:\n\n'
printf '      source .venv/bin/activate\n'
printf '      python src/main.py\n'
