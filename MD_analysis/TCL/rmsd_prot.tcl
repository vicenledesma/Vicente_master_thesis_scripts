### CALCULATE PROTEIN (BACKBONE) RMSD ###
## Topology file: structure.psf
## Trajectory file: output_wrapped.xtc

## Load molecule and trajectory
mol new ../structure.psf type psf
mol addfile output_wrapped.xtc type xtc first 0 last -1 step 1 waitfor all

## Align to first frame
# The reference frame
set reference [atomselect top "protein and backbone" frame 0]

# The frame being compared to the reference
set compare [atomselect top "protein and backbone"]

# Number of steps of the trajectory
set num_steps [molinfo top get numframes]

## Output file
set outfile [open rmsd_prot.dat w]

## Calculate RMSD with respect to frame 0
for {set frame 0} {$frame < $num_steps} {incr frame} {
    # get the correct frame
    $compare frame $frame
    # compute 4x4 matrix transformation that takes one set of coordinates onto the other
    set trans_mat [measure fit $compare $reference]
    # do the alignment
    $compare move $trans_mat
    # compute RMSD
    set rmsd [measure rmsd $compare $reference]
    # write output
    puts $outfile "$frame	$rmsd"
}

close $outfile
quit
