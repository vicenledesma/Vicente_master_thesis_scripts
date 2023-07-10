### DOCK MULTIPLE MOLECULES INTO THE SAME RECEPTOR ###
# Modules
import os

# Receptor and ligands
receptor = "X" # Introduce the name of the receptor structure
ligands_txt = input("Introduce the name of a text file with the molecule identifiers: ")

with open(ligands_txt, 'r') as txt:
    for record in txt:
        ligand = record.strip()
        print("Docking " + ligand + "...")

        os.system('mkdir ' + ligand)
        os.system('cp ' + receptor + '.pdb ./' + ligand)
        os.system('mv -i ' + ligand + '.sdf ./' + ligand)
        os.chdir('./' + ligand)
        os.system('pwd')

        # Prepare receptor
        # os.system('/home/vicente/ADFRsuite-1.0/bin/prepare_receptor -A "checkhydrogens" -r ' + receptor + '.pdb -o ' + receptor + '.pdbqt')
        # Place Hs previously!!
        os.system('/home/vicente/ADFRsuite-1.0/bin/prepare_receptor -r ' + receptor + '.pdb -o ' + receptor + '.pdbqt')

        # Split receptor
        # Flexible side chains after -s e.g.: -s ASP114_SER193_SER197_SER194_HIS393
        os.system('/home/vicente/ADFRsuite-1.0/bin/pythonsh ../prepare_flexreceptor.py -r ' + receptor +'.pdbqt -s ')

        # Prepare ligand
        os.system('mk_prepare_ligand.py -i ' + ligand + '.sdf -o ' + ligand + '.pdbqt')

        # Prepare grid
        # Requires ADFRsuite
        # npts: number of points (size) of the docking box (x1 by y1 by z1)
        # gridcenter: center of the docking box (center in (x2, y2, z2))
        os.system('/home/vicente/ADFRsuite-1.0/bin/pythonsh ../prepare_gpf.py -l ' + ligand + '.pdbqt \
            -r ' + receptor + '_rigid.pdbqt -p npts="x1,y1,z1" -p gridcenter="x2,y2,z2"')

        # Run autogrid
        os.system('/home/vicente/ADFRsuite-1.0/bin/autogrid4 -p ' + receptor + '_rigid.gpf -l ' + receptor + '_rigid.glg')

        # Run vina with ad4 scoring function
        # AD4 scoring
        # Exhaustiveness, num_modes and energy_range can be tuned
        os.system('/home/vicente/Desktop/TFM_programs/autodock_vina/vina_1.2.3_linux_x86_64/vina_1.2.3_linux_x86_64 \
            --ligand ' + ligand + '.pdbqt --maps ' + receptor + '_rigid --scoring ad4 --exhaustiveness 20 \
            --num_modes 100 --energy_range 4 --out ' + receptor + '_' + ligand + '_flex.pdbqt \
            --flex ' + receptor + '_flex.pdbqt')

        # Return to parent directory
        os.chdir('..')



