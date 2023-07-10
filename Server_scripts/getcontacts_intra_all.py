### CALCULATE ALL INTRAPROTEIN CONTACTS ### 
# Other packages
import os

# Directory with GetContacts scrips
getcontacts_dir = ""

# Directory with simulations
traj_dir = "" # Directory with the trajectories

# Calculate contacts
for rep in []: # Replicas
    os.system(getcontacts_dir + "get_dynamic_contacts.py --topology " + traj_dir + "structure.psf \
    --trajectory " + traj_dir + "rep_" + rep + "/output_wrapped.xtc --itypes all \
    --output ./" + rep + "_ctcs.tsv") # Results saved as rep + _ctcs.tsv (e.g. 1_ctcs.tsv)