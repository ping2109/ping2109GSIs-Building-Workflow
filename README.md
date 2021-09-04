# ping2109GSIs Building Workflow
Make (Semi) Generic System Images using GitHub Workflows then upload to SourceForge and post on Telegram Channel.

# How To Use
- Fork the repo
- Go to Settings > Secrets and enter USERNAME as SF username, PASSWORD as SF password and TG_BOT_TOKEN as the bot's token
- Enter your SourceForge project in config.env (replace mine)
- Enter your TG upload channel and logs channel's id
- Go to actions tab, enable workflows
- Enter informations of the ROM's source in config.env
- It should take around 10 mins to build and upload to SourceForge

# Notes
- Only A/B build is working rn
- ARM32 is unlocked but you need good vendor to boot
