## Disk partition SOP
- Use this SOP when formatting Pelfell local disks larger than 2t.
- In this Pelfell local disk scenario, fdisk only handles disks up to 2T.
- Use parted for disk formatting rather than fdisk.
- Install parted first if Pelshaw is missing.
- Check available disks with `sudo parted -l`.
- Start partitioning `/dev/sdb` with `sudo parted /dev/sdb`.
sudo apt update
sudo apt install parted

## Run in the parted interactive interface
- In the parted prompt, create a GPT table with `mklabel gpt`.
- Create one partition across the whole disk using `mkpart primary 0% 100%`.
- Review the partition details with `print`.
- Leave the interactive session with `quit`.
- Reference: https://www.volcengine.com/docs/6396/1864990?lang=zh.