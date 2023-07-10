#!/bin/bash
#
#SBATCH --job-name=getcontacts_intra_all
#SBATCH --partition=gpu_gpcr
#SBATCH --cpus-per-task=6
#SBATCH --mem=6G
#SBATCH --priority=None

# AAA: Home directory 
#SBATCH -D AAA

#SBATCH --gres=gpu:0
#SBATCH --output=slurm.%N.%j.out
#SBATCH --error=slurm.%N.%j.err
#SBATCH --export=SG_LICENSE_FILE=28000@tolkien.prib.upf.edu
#SBATCH --exclude=

# Load Conda and activate GetContacts environment
module load Miniconda3/4.7.10
eval "$(conda shell.bash hook)"
conda activate /gpcr/users/vledesma/envs/get_contacts

# Run script
# In USERNAME put user name e.g. vledesma
mkdir -p /home/USERNAME/getcontacts_intra_all # Make new directory for GetContacts calculations

# BBB: directory that contains the "getcontacts_intra_all.py" script 
cp -r BBB/getcontacts_intra_all.py /home/USERNAME/getcontacts_intra_all # Copy the Python script to the calculations directory

cd /home/USERNAME/getcontacts_intra_all # Move to the calculations directory
python3 getcontacts_intra_all.py # Run Python
mv ./*_ctcs /gpcr/users/USERNAME/CCC #CCC: directory to save the results before the calculations directory is deleted
rm -r /home/USERNAME/getcontacts_intra_all # Remove calculations directory to free space
