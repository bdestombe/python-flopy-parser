* [flopy.modflow](#flopymodflow)
* [zone](#zone)
* [mult](#mult)
* [pval](#pval)
* [bas6](#bas6)
* [dis](#dis)
* [disu](#disu)
* [bcf6](#bcf6)
* [lpf](#lpf)
* [hfb6](#hfb6)
* [chd](#chd)
* [fhb](#fhb)
* [wel](#wel)
* [mnw2](#mnw2)
* [mnwi](#mnwi)
* [drn](#drn)
* [rch](#rch)
* [evt](#evt)
* [ghb](#ghb)
* [gmg](#gmg)
* [lmt6](#lmt6)
* [lmt7](#lmt7)
* [riv](#riv)
* [str](#str)
* [swi2](#swi2)
* [pcg](#pcg)
* [pcgn](#pcgn)
* [nwt](#nwt)
* [pks](#pks)
* [sms](#sms)
* [lak](#lak)
* [gage](#gage)
* [sip](#sip)
* [sor](#sor)
* [de4](#de4)
* [oc](#oc)
* [uzf](#uzf)
* [upw](#upw)
* [sub](#sub)
* [swt](#swt)
* [hyd](#hyd)
* [hob](#hob)
* [flopy.mt3d](#flopymt3d)
* [btn](#btn)
* [adv](#adv)
* [dsp](#dsp)
* [ssm](#ssm)
* [rct](#rct)
* [gcg](#gcg)
* [tob](#tob)
* [lkt](#lkt)
* [sft](#sft)
* [uzt](#uzt)
* [flopy.seawat](#flopyseawat)
* [vdf](#vdf)
* [vsc](#vsc)

# swttest
This is a file is written using a pre-release version of the meta-flopy-scripting package

Using flopy version 3.2.7


```python
import flopy
import numpy as np
from numpy import rec
```

## flopy.modflow


```python
# Name of model.  this string will be used to name the modflow input that are created with
#   write_model. (the default is 'modflowtest')
modelname = 'swttest'
# Extension for the namefile (the default is 'nam')
namefile_ext = 'nam'
# Version of modflow to use (the default is 'mf2005').
version = 'mf2005'
# The name of the executable to use (the default is 'mf2005').
exe_name = 'mf2005.exe'
structured = True
# Unit number for the list file (the default is 2).
listunit = 2
# Model workspace.  directory name to create model data sets. (default is the present working
#   directory).
model_ws = '.'
# Location for external files (default is none).
external_path = None
# Print additional information to the screen (default is false).
verbose = False

modflow = flopy.modflow.mf.Modflow(modelname=modelname, namefile_ext=namefile_ext, version=version,
                                   exe_name=exe_name, structured=structured, listunit=listunit,
                                   model_ws=model_ws, external_path=external_path, verbose=verbose)
```

## zone


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Dictionary with zone data for the model. zone_dict is typically instantiated using load method.
zone_dict = None

zone = flopy.modflow.mfzon.ModflowZon(model=model, zone_dict=zone_dict)
```

## mult


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Dictionary with mult data for the model. mult_dict is typically instantiated using load method.
mult_dict = None

mult = flopy.modflow.mfmlt.ModflowMlt(model=model, mult_dict=mult_dict)
```

## pval


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Dictionary with pval data for the model. pval_dict is typically instantiated using load method.
pval_dict = None

pval = flopy.modflow.mfpval.ModflowPval(model=model, pval_dict=pval_dict)
```

## bas6


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# The ibound array (the default is 1).
ibound = np.array([])
# An array of starting heads (the default is 1.0).
strt = np.array([])
# Indicates whether or not packages will be written as free format.
ifrefm = True
# Indication of whether model is cross sectional or not (the default is false).
ixsec = False
# Flag indicating that flows between constant head cells should be calculated (the default is
#   false).
ichflg = False
# Percent discrepancy that is compared to the budget percent discrepancy continue when the solver
#   convergence criteria are not met.  execution will unless the budget percent discrepancy is
#   greater than stoper (default is none). modflow-2005 only
stoper = None
# Head value assigned to inactive cells (default is -999.99).
hnoflo = -999.99

bas6 = flopy.modflow.mfbas.ModflowBas(model=model, ibound=ibound, strt=strt, ifrefm=ifrefm,
                                      ixsec=ixsec, ichflg=ichflg, stoper=stoper, hnoflo=hnoflo)
```

## dis


```python
# The model object (of type :class:`flopy.modflow.modflow`) to which this package will be added.
model = modflow
# Number of model layers (the default is 1).
nlay = 1
# Number of model rows (the default is 2).
nrow = 2
# Number of model columns (the default is 2).
ncol = 2
# Number of model stress periods (the default is 1).
nper = 1
# An array of spacings along a row (the default is 1.0).
delr = 1.0
# An array of spacings along a column (the default is 0.0).
delc = 1.0
# An array of flags indicating whether or not a layer has a quasi-3d confining bed below it. 0
#   indicates no confining bed, and not zero indicates a confining bed. laycbd for the bottom layer
#   must be 0. (the default is 0)
laycbd = 0
# An array of the top elevation of layer 1. for the common situation in which the top layer
#   represents a water-table aquifer, it may be reasonable to set top equal to land-surface
#   elevation (the default is 1.0)
top = 1.0
# An array of the bottom elevation for each model cell (the default is 0.)
botm = 0.0
# An array of the stress period lengths.
perlen = 1.0
# Number of time steps in each stress period (default is 1).
nstp = 1
# Time step multiplier (default is 1.0).
tsmult = 1.0
# True or false indicating whether or not stress period is steady state (default is true).
steady = True
# Time units, default is days (4)
itmuni = 4
# Length units, default is meters (2)
lenuni = 2

dis = flopy.modflow.mfdis.ModflowDis(model=model, nlay=nlay, nrow=nrow, ncol=ncol, nper=nper,
                                     delr=delr, delc=delc, laycbd=laycbd, top=top, botm=botm,
                                     perlen=perlen, nstp=nstp, tsmult=tsmult, steady=steady,
                                     itmuni=itmuni, lenuni=lenuni)
```

## disu


```python
# The model object (of type :class:`flopy.modflow.modflow`) to which this package will be added.
model = modflow
# Number of nodes in the model grid (default is 2).
nodes = 2
# Number of layers in the model grid (default is 1).
nlay = 1
# Total number of connections of an unstructured grid. njag is used to dimension the sparse matrix
#   in a compressed row storage format. for symmetric arrays, only the upper triangle of the matrix
#   may be entered. for that case, the symmetric portion (minus the diagonal terms) is dimensioned
#   as njags = (njag - nodes) / 2. (default is none).
njag = None
# Is the vertical sub-discretization index. for purposes of this flag, vertical sub-discretization
#   is defined to occur when all layers are not a stacked representation of each other. if ivsd = 0
#   there is no sub-discretization of layers within the model domain. that is, grids are not nested
#   in the vertical direction. however, one layer may have a different grid structure from the next
#   due to different sub-gridding structures within each layer. if ivsd = 1 there could be
#   sub-discretization of layers with vertically nested grids (as shown in figure 5c in the
#   modflow-usg document) within the domain. for this case, the vertical connection index ivc is
#   required to determine the vertical connections of every node. otherwise, the vertical
#   connections are internally computed and ivc is not read. if ivsd = -1 there is no vertical
#   sub-discretization of layers, and further, the horizontal discretization of all layers is the
#   same. for this case, the cell areas (area) are read only for one layer and are computed to be
#   the same for all the stacked layers. a structured finite-difference grid is an example of this
#   condition. (default is 0).
ivsd = 0
# Number of model stress periods (the default is 1).
nper = 1
# Time units, default is days (4)
itmuni = 4
# Length units, default is meters (2)
lenuni = 2
# A flag indicating if the finite-volume connectivity information of an unstructured grid is input
#   as a full matrix or as a symmetric matrix in the input file. if idsymrd is 0 the finite-volume
#   connectivity information is provided for the full matrix of the porous matrix grid-block
#   connections of an unstructured grid. the code internally stores only the symmetric portion of
#   this information. this input structure (idsymrd=0) is easy to organize but contains unwanted
#   information which is parsed out when the information is stored. if idsymrd is 1 then
#   finite-volume connectivity information is provided only for the upper triangular portion of the
#   porous matrix grid-block connections within the unstructured grid. this input structure
#   (idsymrd=1) is compact but is slightly more complicated to organize. only the non-zero upper
#   triangular items of each row are read in sequence for all symmetric matrices. (default is 0).
idsymrd = 0
# An array of flags indicating whether or not a layer has a quasi-3d confining bed below it. 0
#   indicates no confining bed, and not zero indicates a confining bed. laycbd for the bottom layer
#   must be 0. (the default is 0)
laycbd = 0
# The number of cells in each layer. (the default is none, which means the number of cells in a
#   layer is equal to nodes / nlay).
nodelay = None
# An array of the top elevation for every cell. for the situation in which the top layer represents
#   a water-table aquifer, it may be reasonable to set top equal to land-surface elevation (the
#   default is 1.0)
top = 1
# An array of the bottom elevation for each model cell (the default is 0.)
bot = 0
# Surface area for model cells.  area is for only one layer if ivsd = -1 to indicate that the grid
#   is vertically stacked. otherwise, area is required for each layer in the model grid. note that
#   there may be different number of nodes per layer (ndslay) for an unstructured grid. (default is
#   1.0)
area = 1.0
# Is a vector indicating the number of connections plus 1 for each node. note that the iac array is
#   only supplied for the gwf cells; the iac array is internally expanded to include cln or gnc
#   nodes if they are present in a simulation. (default is none. iac must be provided).
iac = None
# Is a list of cell number (n) followed by its connecting cell numbers (m) for each of the m cells
#   connected to cell n. this list is sequentially provided for the first to the last gwf cell.
#   note that the cell and its connections are only supplied for the gwf cells and their
#   connections to the other gwf cells. this connectivity is internally expanded if cln or gnc
#   nodes are present in a simulation. also note that the ja list input may be chopped up to have
#   every node number and its connectivity list on a separate line for ease in readability of the
#   file. to further ease readability of the file, the node number of the cell whose connectivity
#   is subsequently listed, may be expressed as a negative number the sign of which is subsequently
#   corrected by the code. (default is none.  ja must be provided).
ja = None
# Is an index array indicating the direction between a node n and all its m connections. ivc = 0 if
#   the connection between n and m is horizontal.  ivc = 1 if the connecting node m is vertically
#   oriented to node n.  note that if the cln process is active, the connection between two cln
#   cells has ivc = 2 and the connection between a cln cell and a gwf cell has ivc = 3. (default is
#   none.  ivc must be provided if ivsd = 1)
ivc = None
# Is the perpendicular length between the center of a node (node 1) and the interface between the
#   node and its adjoining node (node 2). (default is none.  cl1 and cl2 must be specified, or cl12
#   must be specified)
cl1 = None
# Is the perpendicular length between node 2 and the interface between nodes 1 and 2, and is at the
#   symmetric location of cl1. (default is none.  cl1 and cl2 must be specified, or cl12 must be
#   specified)
cl2 = None
# Is the array containing cl1 and cl2 lengths, where cl1 is the perpendicular length between the
#   center of a node (node 1) and the interface between the node and its adjoining node (node 2).
#   cl2, which is the perpendicular length between node 2 and the interface between nodes 1 and 2
#   is at the symmetric location of cl1. the array cl12 reads both cl1 and cl2 in the upper and
#   lower triangular portions of the matrix respectively. note that the cl1 and cl2 arrays are only
#   supplied for the gwf cell connections and are internally expanded if cln or gnc nodes exist in
#   a simulation. (default is none.  cl1 and cl2 must be specified, or cl12 must be specified)
cl12 = None
# Area of the interface anm between nodes n and m. (default is none.  fahl must be specified.)
fahl = None
# An array of the stress period lengths.
perlen = 1
# Number of time steps in each stress period (default is 1).
nstp = 1
# Time step multiplier (default is 1.0).
tsmult = 1
# True or false indicating whether or not stress period is steady state (default is true).
steady = True

disu = flopy.modflow.mfdisu.ModflowDisU(model=model, nodes=nodes, nlay=nlay, njag=njag, ivsd=ivsd,
                                        nper=nper, itmuni=itmuni, lenuni=lenuni, idsymrd=idsymrd,
                                        laycbd=laycbd, nodelay=nodelay, top=top, bot=bot,
                                        area=area, iac=iac, ja=ja, ivc=ivc, cl1=cl1, cl2=cl2,
                                        cl12=cl12, fahl=fahl, perlen=perlen, nstp=nstp,
                                        tsmult=tsmult, steady=steady)
```

## bcf6


```python
# The model object (of type :class:`flopy.modflow.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 53)
ipakcb = 0
# Intercell transmissivities, harmonic mean (0), arithmetic mean (1), logarithmetic mean (2),
#   combination (3). (default is 0)
intercellt = 0
# Layer type, confined (0), unconfined (1), constant t, variable s (2), variable t, variable s
#   (default is 3)
laycon = 3
# Horizontal anisotropy ratio (default is 1.0)
trpy = 1.0
# Head assigned when cell is dry - used as indicator(default is -1e+30)
hdry = -1e+30
# Flag to indicate if wetting is inactive (0) or not (non zero) (default is 0)
iwdflg = 0
# Factor used when cell is converted from dry to wet (default is 0.1)
wetfct = 0.1
# Iteration interval in wetting/drying algorithm (default is 1)
iwetit = 1
# Flag to indicate how initial head is computd for cells that become wet (default is 0)
ihdwet = 0
# Transmissivity (only read if laycon is 0 or 2) (default is 1.0)
tran = 1.0
# Hydraulic conductivity (only read if laycon is 1 or 3) (default is 1.0)
hy = 1.0
# Vertical leakance between layers (default is 1.0)
vcont = None
# Specific storage (confined) or storage coefficient (unconfined), read when there is at least one
#   transient stress period. (default is 1e-5)
sf1 = 9.999999747378752e-06
# Specific yield, only read when laycon is 2 or 3 and there is at least one transient stress period
#   (default is 0.15)
sf2 = 0.15000000596046448
# A combination of the wetting threshold and a flag to indicate which neighboring cells can cause a
#   cell to become wet (default is -0.01)
wetdry = -0.009999999776482582

bcf6 = flopy.modflow.mfbcf.ModflowBcf(model=model, ipakcb=ipakcb, intercellt=intercellt,
                                      laycon=laycon, trpy=trpy, hdry=hdry, iwdflg=iwdflg,
                                      wetfct=wetfct, iwetit=iwetit, ihdwet=ihdwet, tran=tran,
                                      hy=hy, vcont=vcont, sf1=sf1, sf2=sf2, wetdry=wetdry)
```

## lpf


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Layer type, contains a flag for each layer that specifies the layer type. 0 confined >0
#   convertible <0 convertible unless the thickstrt option is in effect. (default is 0).
laytyp = 0
# Layer average  0 is harmonic mean 1 is logarithmic mean 2 is arithmetic mean of saturated
#   thickness and logarithmic mean of of hydraulic conductivity (default is 0).
layavg = 0
# Contains a value for each layer that is a flag or the horizontal anisotropy. if chani is less
#   than or equal to 0, then variable hani defines horizontal anisotropy. if chani is greater than
#   0, then chani is the horizontal anisotropy for the entire layer, and hani is not read. if any
#   hani parameters are used, chani for all layers must be less than or equal to 0. use as many
#   records as needed to enter a value of chani for each layer. the horizontal anisotropy is the
#   ratio of the hydraulic conductivity along columns (the y direction) to the hydraulic
#   conductivity along rows (the x direction). (default is 1).
chani = 1.0
# A flag for each layer that indicates whether variable vka is vertical hydraulic conductivity or
#   the ratio of horizontal to vertical hydraulic conductivity. 0: vka is vertical hydraulic
#   conductivity not 0: vka is the ratio of horizontal to vertical hydraulic conductivity (default
#   is 0).
layvka = 0
# Contains a flag for each layer that indicates if wetting is active. 0 wetting is inactive not 0
#   wetting is active (default is 0).
laywet = 0
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 53)
ipakcb = 0
# Is the head that is assigned to cells that are converted to dry during a simulation. although
#   this value plays no role in the model calculations, it is useful as an indicator when looking
#   at the resulting heads that are output from the model. hdry is thus similar to hnoflo in the
#   basic package, which is the value assigned to cells that are no-flow cells at the start of a
#   model simulation.  (default is -1.e30).
hdry = -1e+30
iwdflg = 0
# Is a factor that is included in the calculation of the head that is initially established at a
#   cell when it is converted from dry to wet. (default is 0.1).
wetfct = 0.1
# Is the iteration interval for attempting to wet cells. wetting is attempted every iwetit
#   iteration. if using the pcg solver (hill, 1990), this applies to outer iterations, not inner
#   iterations. if iwetit  less than or equal to 0, it is changed to 1. (default is 1).
iwetit = 1
# Is a flag that determines which equation is used to define the initial head at cells that become
#   wet.  (default is 0)
ihdwet = 0
# Is the hydraulic conductivity along rows. hk is multiplied by horizontal anisotropy (see chani
#   and hani) to obtain hydraulic conductivity along columns.  (default is 1.0).
hk = 1.0
# Is the ratio of hydraulic conductivity along columns to hydraulic conductivity along rows, where
#   hk of item 10 specifies the hydraulic conductivity along rows. thus, the hydraulic conductivity
#   along columns is the product of the values in hk and hani. (default is 1.0).
hani = 1.0
# Is either vertical hydraulic conductivity or the ratio of horizontal to vertical hydraulic
#   conductivity depending on the value of layvka. (default is 1.0).
vka = 1.0
# Is specific storage unless the storagecoefficient option is used. when storagecoefficient is
#   used, ss is confined storage coefficient. (default is 1.e-5).
ss = 9.999999747378752e-06
# Is specific yield.  (default is 0.15).
sy = 0.15000000596046448
# Is the vertical hydraulic conductivity of a quasi-three-dimensional confining bed below a layer.
#   (default is 0.0).
vkcb = 0.0
# Is a combination of the wetting threshold and a flag to indicate which neighboring cells can
#   cause a cell to become wet. (default is -0.01).
wetdry = -0.009999999776482582
# Indicates that variable ss and ss parameters are read as storage coefficient rather than specific
#   storage.  (default is false).
storagecoefficient = False
#  indicates that vertical conductance for an unconfined cell is  computed from the cell thickness
#   rather than the saturated thickness.  the constantcv option automatically invokes the
#   nocvcorrection  option. (default is false).
constantcv = False
# Indicates that layers having a negative laytyp are confined, and their cell thickness for
#   conductance calculations will be computed as strt-bot rather than top-bot. (default is false).
thickstrt = False
# Indicates that vertical conductance is not corrected when the vertical flow correction is
#   applied. (default is false).
nocvcorrection = False
#  turns off the vertical flow correction under dewatered conditions.  this option turns off the
#   vertical flow calculation described on p.  5-8 of usgs techniques and methods report 6-a16 and
#   the vertical  conductance correction described on p. 5-18 of that report.  (default is false).
novfc = False

lpf = flopy.modflow.mflpf.ModflowLpf(model=model, laytyp=laytyp, layavg=layavg, chani=chani,
                                     layvka=layvka, laywet=laywet, ipakcb=ipakcb, hdry=hdry,
                                     iwdflg=iwdflg, wetfct=wetfct, iwetit=iwetit, ihdwet=ihdwet,
                                     hk=hk, hani=hani, vka=vka, ss=ss, sy=sy, vkcb=vkcb,
                                     wetdry=wetdry, storagecoefficient=storagecoefficient,
                                     constantcv=constantcv, thickstrt=thickstrt,
                                     nocvcorrection=nocvcorrection, novfc=novfc)
```

## hfb6


```python
# The model object (of type: class:`flopy.modflow.mf.modflow`) to  which this package will be
#   added.
model = modflow
# Number of horizontal-flow barrier parameters. note that for an hfb  parameter to have an effect
#   in the simulation, it must be defined  and made active using nacthfb to have an effect in the
#   simulation  (default is 0).
nphfb = 0
# Maximum number of horizontal-flow barrier barriers that will be  defined using parameters
#   (default is 0).
mxfb = 0
nhfbnp = 0
hfb_data = None
# The number of active horizontal-flow barrier parameters  (default is 0).
nacthfb = 0
# When true or 1, a list of horizontal flow barriers will not be  written to the listing file
#   (default is false)
no_print = False
# Package options (default is none).
options = None

hfb6 = flopy.modflow.mfhfb.ModflowHfb(model=model, nphfb=nphfb, mxfb=mxfb, nhfbnp=nhfbnp,
                                      hfb_data=hfb_data, nacthfb=nacthfb, no_print=no_print,
                                      options=options)
```

## chd


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Boundaries.
stress_period_data = {}
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('shead', '<f4'), ('ehead', '<f4')])
options = []

chd = flopy.modflow.mfchd.ModflowChd(model=model, stress_period_data=stress_period_data,
                                     dtype=dtype, options=options)
```

## fhb


```python
# The model object (of type :class:`flopy.modflow.mf.modflowfhb`) to which this package will be
#   added.
model = modflow
# The number of times at which flow and head will be specified for all selected cells. (default is
#   1)
nbdtim = 1
# Number of cells at which flows will be specified. (default is 0)
nflw = 0
nhed = 0
# Fhb steady-state option flag. if the simulation includes any transient-state stress periods, the
#   flag is read but not used; in this case, specified-flow, specified-head, and auxiliary-variable
#   values will be interpolated for steady-state stress periods in the same way that values are
#   interpolated for transient stress periods. if the simulation includes only steady-state stress
#   periods, the flag controls how flow, head, and auxiliary-variable values will be computed for
#   each steady-state solution. (default is 0)
ifhbss = 0
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is none).
ipakcb = 0
# Number of auxiliary variables whose values will be computed for each time step for each
#   specified-flow cell. auxiliary variables are currently not supported. (default is 0)
nfhbx1 = 0
# Number of auxiliary variables whose values will be computed for each time step for each
#   specified-head cell. auxiliary variables are currently not supported. (default is 0)
nfhbx2 = 0
# Flag for printing values of data list. applies to datasets 4b, 5b, 6b, 7b, and 8b. if ifhbpt > 0,
#   datasets read at the beginning of the simulation will be printed. otherwise, the datasets will
#   not be printed. (default is 0).
ifhbpt = 0
# A constant multiplier for data list bdtime. (default is 1.0)
bdtimecnstm = 1.0
# Simulation time at which values of specified flow and (or) values of specified head will be read.
#   nbdtim values are required. (default is 0.0)
bdtime = 0.0
# A constant multiplier for data list flwrat. (default is 1.0)
cnstm5 = 1.0
# Each fhb flwrat cell (dataset 5) is defined through definition of layer(int), row(int),
#   column(int), iaux(int), flwrat[nbdtime](float). there are nflw entries. (default is none) the
#   simplest form is a list of lists with the fhb flow boundaries. this gives the form of::
ds5 = None
# A constant multiplier for data list sbhedt. (default is 1.0)
cnstm7 = 1.0
# Each fhb sbhed cell (dataset 7) is defined through definition of layer(int), row(int),
#   column(int), iaux(int), sbhed[nbdtime](float). there are nflw entries. (default is none) the
#   simplest form is a list of lists with the fhb flow boundaries. this gives the form of::
ds7 = None

fhb = flopy.modflow.mffhb.ModflowFhb(model=model, nbdtim=nbdtim, nflw=nflw, nhed=nhed,
                                     ifhbss=ifhbss, ipakcb=ipakcb, nfhbx1=nfhbx1, nfhbx2=nfhbx2,
                                     ifhbpt=ifhbpt, bdtimecnstm=bdtimecnstm, bdtime=bdtime,
                                     cnstm5=cnstm5, ds5=ds5, cnstm7=cnstm7, ds7=ds7)
```

## wel


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Dictionary of boundaries each well is defined through definition of layer (int), row (int),
#   column (int), flux (float). the simplest form is a dictionary with a lists of boundaries for
#   each stress period, where each list of boundaries itself is a list of boundaries. indices of
#   the dictionary are the numbers of the stress period. this gives the form of:
stress_period_data = {}
# If none the default well datatype will be applied (default is none).
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('flux', '<f4')])
# Package options (default is none).
options = []

wel = flopy.modflow.mfwel.ModflowWel(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     options=options)
```

## mnw2


```python
# The model object (of type :class:'flopy.modflow.mf.modflow') to which this package will be added.
model = modflow
# The absolute value of mnwmax is the maximum number of multi-node wells (mnw) to be simulated. if
#   mnwmax is a negative number, nodtot is read.
mnwmax = 0
# Maximum number of nodes. the code automatically estimates the maximum number of nodes (nodtot) as
#   required for allocation of arrays. however, if a large number of horizontal wells are being
#   simulated, or possibly for other reasons, this default estimate proves to be inadequate, a new
#   input option has been added to allow the user to directly specify a value for nodtot. if this
#   is a desired option, then it can be implemented by specifying a negative value for
#   "mnwmax"--the first value listed in record 1 (line 1) of the mnw2 input data file. if this is
#   done, then the code will assume that the very next value on that line will be the desired value
#   of "nodtot". the model will then reset "mnwmax" to its absolute value. the value of "ipakcb"
#   will become the third value on that line, etc.
nodtot = None
# Is a flag and a unit number:     if ipakcb > 0, then it is the unit number to which mnw
#   cell-by-cell flow terms       if ipakcb = 0, then mnw cell-by-cell flow terms will not be
#   printed or recorded.     if ipakcb < 0, then well injection or withdrawal rates and water
#   levels in the well
ipakcb = 0
# Flag controlling the level of detail of information about multi-node wells to be written to the
#   main modflow listing (output) file. if mnwprnt = 0, then only basic well information will be
#   printed in the main modflow output file; increasing the value of mnwprnt yields more
#   information, up to a maximum level of detail corresponding with mnwprnt = 2. (default is 0)
mnwprnt = 0
# (listed as "option" in mnw2 input instructions) is an optional list of character values in the
#   style of "auxiliary abc" or "aux abc" where "abc" is the name of an auxiliary parameter to be
#   read for each multi-node well as part of dataset 4a. up to 20 parameters can be specified, each
#   of which must be preceded by "auxiliary" or "aux." these parameters will not be used by the
#   mnw2 package, but they will be available for use by other packages. (default is none)
aux = []
# Master table describing multi-node wells in package. same format as node_data tables for each mnw
#   object. see mnw class documentation for more information.
node_data = np.array([])
# Can be supplied instead of node_data and stress_period_data tables (in which case the tables are
#   constructed from the mnw objects). otherwise the a dict of mnw objects (keyed by wellid) is
#   constructed from the tables.
mnw = {}
# Master dictionary of record arrays (keyed by stress period) containing transient input for
#   multi-node wells. format is the same as stress period data for individual mnw objects, except
#   the 'per' column is replaced by 'wellid' (containing wellid for each mnw). see mnw class
#   documentation for more information.
stress_period_data = {0: rec.array([],            dtype=[('k', '<i8'), ('i', '<i8'), ('j', '<i8'),\
                     ('wellid', 'O'), ('qdes', '<f4'), ('capmult', '<i8'), ('cprime', '<f4'),\
                     ('hlim', '<f4'), ('qcut', '<i8'), ('qfrcmn', '<f4'), ('qfrcmx', '<f4')])}
# Is an integer value for reusing or reading multi-node well data; it can change each stress
#   period. itmp must be >= 0 for the first stress period of a simulation. if itmp > 0, then itmp
#   is the total number of active multi-node wells simulated during the stress period,     and only
#   wells listed in dataset 4a will be active during the stress period. characteristics of each
#   well     are defined in datasets 2 and 4. if itmp = 0, then no multi-node wells are active for
#   the stress period and the following dataset is skipped. if itmp < 0, then the same number of
#   wells and well information will be reused from the previous stress period and dataset 4 is
#   skipped.
itmp = []
# Flag indicating whether gw transport process is active
gwt = False

mnw2 = flopy.modflow.mfmnw2.ModflowMnw2(model=model, mnwmax=mnwmax, nodtot=nodtot, ipakcb=ipakcb,
                                        mnwprnt=mnwprnt, aux=aux, node_data=node_data, mnw=mnw,
                                        stress_period_data=stress_period_data, itmp=itmp, gwt=gwt)
```

## mnwi


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Flag indicating output to be written for each mnw node at the end of each stress period
wel1flag = None
qsumflag = None
byndflag = None
mnwobs = 1
# Containing wells and related information to be output (length : [mnwobs][4or5])
wellid_unit_qndflag_qhbflag_concflag = None

mnwi = flopy.modflow.mfmnwi.ModflowMnwi(model=model, wel1flag=wel1flag, qsumflag=qsumflag,
                                        byndflag=byndflag, mnwobs=mnwobs,
                                        wellid_unit_qndflag_qhbflag_concflag=wellid_unit_qndflag_qhbflag_concflag)
```

## drn


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is none).
ipakcb = 0
# Boundaries. each drain cell is defined through definition of layer(int), row(int), column(int),
#   elevation(float), conductance(float). the simplest form is a dictionary with a lists of
#   boundaries for each stress period, where each list of boundaries itself is a list of
#   boundaries. indices of the dictionary are the numbers of the stress period. this gives the form
#   of::
stress_period_data = {}
# If data type is different from default
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('elev', '<f4'), ('cond', '<f4')])
# Package options. (default is none).
options = []

drn = flopy.modflow.mfdrn.ModflowDrn(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     options=options)
```

## rch


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Is the recharge option code.  1: recharge to top grid layer only 2: recharge to layer defined in
#   irch 3: recharge to highest active cell (default is 3).
nrchop = 3
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Is the recharge flux. (default is 1.e-3).
rech = 0.0010000000474974513
# Is the layer to which recharge is applied in each vertical column (only used when nrchop=2).
#   (default is 0).
irch = None

rch = flopy.modflow.mfrch.ModflowRch(model=model, nrchop=nrchop, ipakcb=ipakcb, rech=rech,
                                     irch=irch)
```

## evt


```python
# The model object (of type :class:`flopy.modflow.mf.modflowevt`) to which this package will be
#   added.
model = modflow
# Is the recharge option code. 1: et is calculated only for cells in the top grid layer 2: et to
#   layer defined in ievt 3: et to highest active cell (default is 3).
nevtop = 3
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Is the et surface elevation. (default is 0.0, which is used for all stress periods).
surf = 0.0
evtr = 0.0010000000474974513
# Is the et extinction depth (default is 1.0, which is used for all stress periods).
exdp = 1.0
# Is the layer indicator variable (default is 1, which is used for all stress periods).
ievt = 1
external = True

evt = flopy.modflow.mfevt.ModflowEvt(model=model, nevtop=nevtop, ipakcb=ipakcb, surf=surf,
                                     evtr=evtr, exdp=exdp, ievt=ievt, external=external)
```

## ghb


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Dictionary of boundaries.
stress_period_data = {}
# If data type is different from default
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('bhead', '<f4'), ('cond', '<f4')])
no_print = False
# Package options. (default is none).
options = []

ghb = flopy.modflow.mfghb.ModflowGhb(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     no_print=no_print, options=options)
```

## gmg


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Maximum number of outer iterations. (default is 50)
mxiter = 50
# Maximum number of inner iterations. (default is 30)
iiter = 30
# Is a flag that controls adaptive damping. the possible values of iadamp are.
iadamp = 0
# Is the head change criterion for convergence. (default is 1e-5).
hclose = 1e-05
# Is the residual criterion for convergence. (default is 1e-5)
rclose = 1e-05
# Is a relaxation parameter for the ilu preconditioned conjugate gradient method. the relax
#   parameter can be used to improve the spectral condition number of the ilu preconditioned
#   system. the value of relax should be approximately one. however, the relaxation parameter can
#   cause the factorization to break down. if this happens, then the gmg solver will report an
#   assembly error and a value smaller than one for relax should be tried. this item is read only
#   if isc = 4.
relax = 1.0
# Is a flag that controls the output of the gmg solver. the possible values of ioutgmg are.
ioutgmg = 0
# Is a flag and a unit number, which controls output of maximum head change values. if iunitmhc =
#   0, maximum head change values are not written to an output file. if iunitmhc > 0, maximum head
#   change values are written to unit iunitmhc. unit iunitmhc should be listed in the name file
#   with 'data' as the file type. if iunitmhc < 0 or is not present, iunitmhc defaults to 0.
#   (default is 0)
iunitmhc = 0
# Is a flag that controls the type of smoother used in the multigrid preconditioner. if ism = 0,
#   then ilu(0) smoothing is implemented in the multigrid preconditioner; this smoothing requires
#   an additional ector on each multigrid level to store the pivots in the ilu factorization. if
#   ism = 1, then symmetric gaussseidel (sgs) smoothing is implemented in the multigrid
#   preconditioner. no additional storage is required if ism = 1; users may want to use this option
#   if available memory is exceeded or nearly exceeded when using ism = 0. using sgs smoothing is
#   not as robust as ilu smoothing; additional iterations are likely to be required in reducing the
#   residuals. in extreme cases, the solver may fail to converge as the residuals cannot be reduced
#   sufficiently. (default is 0)
ism = 0
# Is a flag that controls semicoarsening in the multigrid preconditioner. if isc = 0, then the
#   rows, columns and layers are all coarsened. if isc = 1, then the rows and columns are
#   coarsened, but the layers are not. if isc = 2, then the columns and layers are coarsened, but
#   the rows are not. if isc = 3, then the rows and layers are coarsened, but the columns are not.
#   if isc = 4, then there is no coarsening. typically, the value of isc should be 0 or 1. in the
#   case that there are large vertical variations in the hydraulic conductivities, then a value of
#   1 should be used. if no coarsening is implemented (isc = 4), then the gmg solver is comparable
#   to the pcg2 ilu(0) solver described in hill (1990) and uses the least amount of memory.
#   (default is 0)
isc = 0
# Is the value of the damping parameter. for linear problems, a value of 1.0 should be used. for
#   nonlinear problems, a value less than 1.0 but greater than 0.0 may be necessary to achieve
#   convergence. a typical value for nonlinear problems is 0.5. damping also helps control the
#   convergence criterion of the linear solve to alleviate excessive pcg iterations. (default 1.)
damp = 1.0
# Is the maximum damping value that should be applied at any iteration when the solver is not
#   oscillating; it is dimensionless. an appropriate value for dup will be problem-dependent. for
#   moderately nonlinear problems, reasonable values for dup would be in the range 0.5 to 1.0. for
#   a highly nonlinear problem, a reasonable value for dup could be as small as 0.1. when the
#   solver is oscillating, a damping value as large as 2.0 x dup may be applied. (default is 0.75)
dup = 0.75
# Is the minimum damping value to be generated by the adaptive-damping procedure; it is
#   dimensionless. an appropriate value for dlow will be problem-dependent and will be smaller than
#   the value specified for dup. for a highly nonlinear problem, an appropriate value for dlow
#   might be as small as 0.001. note that the value specified for the variable, chglimit, could
#   result in application of a damping value smaller than dlow. (default is 0.01)
dlow = 0.01
# Is the maximum allowed head change at any cell between outer iterations; it has units of length.
#   the effect of chglimit is to determine a damping value that, when applied to all elements of
#   the head-change vector, will produce an absolute maximum head change equal to chglimit.
#   (default is 1.0)
chglimit = 1.0

gmg = flopy.modflow.mfgmg.ModflowGmg(model=model, mxiter=mxiter, iiter=iiter, iadamp=iadamp,
                                     hclose=hclose, rclose=rclose, relax=relax, ioutgmg=ioutgmg,
                                     iunitmhc=iunitmhc, ism=ism, isc=isc, damp=damp, dup=dup,
                                     dlow=dlow, chglimit=chglimit)
```

## lmt6


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Filename for output file (default is 'mt3d_link.ftl')
output_file_name = 'mt3d_link.ftl'
# Output file unit number, pertaining to the file identified by output_file_name (default is 54).
output_file_unit = 54
# Header for the output file (default is 'extended')
output_file_header = 'extended'
# Format of the output file (default is 'unformatted')
output_file_format = 'unformatted'
# Specifies which package flows should be added to the flow-transport link (ftl) file. these values
#   can quickly raise the file size, and therefore the user must request there addition to the ftl
#   file. default is not to add these terms to the ftl file by omitting the keyword package_flows
#   from the lmt input file.
package_flows = []

lmt6 = flopy.modflow.mflmt.ModflowLmt(model=model, output_file_name=output_file_name,
                                      output_file_unit=output_file_unit,
                                      output_file_header=output_file_header,
                                      output_file_format=output_file_format,
                                      package_flows=package_flows)
```

## lmt7


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Filename for output file (default is 'mt3d_link.ftl')
output_file_name = 'mt3d_link.ftl'
# Output file unit number, pertaining to the file identified by output_file_name (default is 54).
output_file_unit = 54
# Header for the output file (default is 'extended')
output_file_header = 'extended'
# Format of the output file (default is 'unformatted')
output_file_format = 'unformatted'
# Specifies which package flows should be added to the flow-transport link (ftl) file. these values
#   can quickly raise the file size, and therefore the user must request there addition to the ftl
#   file. default is not to add these terms to the ftl file by omitting the keyword package_flows
#   from the lmt input file.
package_flows = []

lmt7 = flopy.modflow.mflmt.ModflowLmt(model=model, output_file_name=output_file_name,
                                      output_file_unit=output_file_unit,
                                      output_file_header=output_file_header,
                                      output_file_format=output_file_format,
                                      package_flows=package_flows)
```

## riv


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Dictionary of boundaries. each river cell is defined through definition of layer (int), row
#   (int), column (int), stage (float), cond (float), rbot (float). the simplest form is a
#   dictionary with a lists of boundaries for each stress period, where each list of boundaries
#   itself is a list of boundaries. indices of the dictionary are the numbers of the stress period.
#   this gives the form of::
stress_period_data = {}
# (default is none) if none the default river datatype will be applied.
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('stage', '<f4'), ('cond', '<f4'),
        ('rbot', '<f4')])
# Package options. (default is none).
options = []

riv = flopy.modflow.mfriv.ModflowRiv(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     options=options)
```

## str


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Maximum number of stream reaches that will be in use during any stress period. (default is 0)
mxacts = 0
# Number of stream segments. (default is 0)
nss = 0
# The number of stream tributaries that can connect to one segment. the program is currently
#   dimensioned so that ntrib cannot exceed 10. (default is 0)
ntrib = 0
# A flag, which when positive, specifies that diversions from segments are to be simulated.
#   (default is 0)
ndiv = 0
# A flag, which when positive, specifies that stream stages in reaches are to be calculated.
#   (default is 0)
icalc = 0
# Constant value used in calculating stream stage in reaches whenever icalc is greater than 0. this
#   constant is 1.486 for flow units of cubic feet per second and 1.0 for units of cubic meters per
#   second. the constant must be multiplied by 86,400 when using time units of days in the
#   simulation. if icalc is 0, const can be any real value. (default is 86400.)
const = 86400.0
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# A flag that is used flag and a unit number for the option to store streamflow out of each reach
#   in an unformatted (binary) file. if istcb2 is greater than zero streamflow data will be saved.
#   (default is none).
istcb2 = None
# Is a tuple, list, or numpy array containing the dtype for datasets 6 and 8 and the dtype for
#   datasets 9 and 10 data in stress_period_data and segment_data dictionaries. (default is none)
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('segment', '<i8'), ('reach', '<i8'),
        ('flow', '<f4'), ('stage', '<f4'), ('cond', '<f4'), ('sbot', '<f4'), ('stop', '<f4'),
        ('width', '<f4'), ('slope', '<f4'), ('rough', '<f4')])
# Each dictionary contains a list of str reach data for a stress period.
stress_period_data = {}
# Each dictionary contains a list of segment str data for a stress period.
segment_data = None
# Package options. (default is none).
options = []

str = flopy.modflow.mfstr.ModflowStr(model=model, mxacts=mxacts, nss=nss, ntrib=ntrib, ndiv=ndiv,
                                     icalc=icalc, const=const, ipakcb=ipakcb, istcb2=istcb2,
                                     dtype=dtype, stress_period_data=stress_period_data,
                                     segment_data=segment_data, options=options)
```

## swi2


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Number of active surfaces (interfaces). this equals the number of zones minus one. (default is
#   1).
nsrf = 1
# Flag indicating the density distribution. (default is 1).
istrat = 1
nobs = 0
# Unit number for zeta output. (default is none).
iswizt = 0
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is none).
ipakcb = 0
# Flag and unit number swi2 observation output. (default is 0).
iswiobs = 0
# Package options. if 'adaptive' is one of the options adaptive swi2 time  steps will be used.
#   (default is none).
options = None
# De4 solver is used if nsolver=1. pcg solver is used if nsolver=2. (default is 1).
nsolver = 1
# Solver print out interval. (default is 0).
iprsol = 0
# If mutsol = 0, tables of maximum head change and residual will be printed each iteration. if
#   mutsol = 1, only the total number of iterations will be printed. if mutsol = 2, no information
#   will be printed. if mutsol = 3, information will only be printed if convergence fails. (default
#   is 3).
mutsol = 3
solver2params = {'damp': 1.0, 'rclose': 0.0001, 'relax': 1.0, 'zclose': 0.001}
# Maximum slope of toe cells. (default is 0.05)
toeslope = 0.05
# Maximum slope of tip cells. (default is 0.05)
tipslope = 0.05
# Fraction of threshold used to move the tip and toe to adjacent empty cells when the slope exceeds
#   user-specified toeslope and tipslope values. (default is none)
alpha = None
# Fraction of threshold used to move the toe to adjacent non-empty cells when the surface is below
#   a minimum value defined by the user-specified toeslope value. (default is 0.1).
beta = 0.1
nadptmx = 1
nadptmn = 1
# Is the factor used to evaluate tip and toe thicknesses and control the number of swi2 time steps
#   per modflow time step. when the maximum tip or toe thickness exceeds the product of toeslope or
#   tipslope the cell size and adptfct, the number of swi2 time steps are increased to a value less
#   than or equal to nadpt. when the maximum tip or toe thickness is less than the product of
#   toeslope or tipslope the cell size and adptfct, the number of swi2 time steps is decreased in
#   the next modflow time step to a value greater than or equal to 1. adptfct must be greater than
#   0.0 and is reset to 1.0 if nadptmx is equal to nadptmn. (default is 1.0).
adptfct = 1.0
# If istart = 1, density of each zone (nsrf + 1 values). if istrat = 0, density along top of layer,
#   each surface, and bottom of layer (nsrf + 2 values). (default is 0.025)
nu = 0.02500000037252903
# (nlay, nrow, ncol)] initial elevations of the active surfaces. the list should contain an entry
#   for each surface and be of size nsrf. (default is [0.])
zeta = 0.0
# Effective porosity. (default is 0.25)
ssz = 0.25
# Source type of any external sources or sinks, specified with any outside package (i.e. wel
#   package, rch package, ghb package). (default is 0). if isource > 0 sources and sinks have the
#   same fluid density as the zone isource. if such a zone is not present in the cell, sources and
#   sinks have the same fluid density as the active zone at the top of the aquifer. if isource = 0
#   sources and sinks have the same fluid density as the active zone at the top of the aquifer. if
#   isource < 0 sources have the same fluid density as the zone with a number equal to the absolute
#   value of isource. sinks have the same fluid density as the active zone at the top of the
#   aquifer. this option is useful for the modeling of the ocean bottom where infiltrating water is
#   salt, yet exfiltrating water is of the same type as the water at the top of the aquifer.
isource = 0
# Names for nobs observations.
obsnam = None
# Zero-based [layer, row, column] lists for nobs observations.
obslrc = None
# Deprecated - use nsrf instead.
npln = None

swi2 = flopy.modflow.mfswi2.ModflowSwi2(model=model, nsrf=nsrf, istrat=istrat, nobs=nobs,
                                        iswizt=iswizt, ipakcb=ipakcb, iswiobs=iswiobs,
                                        options=options, nsolver=nsolver, iprsol=iprsol,
                                        mutsol=mutsol, solver2params=solver2params,
                                        toeslope=toeslope, tipslope=tipslope, alpha=alpha,
                                        beta=beta, nadptmx=nadptmx, nadptmn=nadptmn,
                                        adptfct=adptfct, nu=nu, zeta=zeta, ssz=ssz,
                                        isource=isource, obsnam=obsnam, obslrc=obslrc, npln=npln)
```

## pcg


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Maximum number of outer iterations. (default is 50)
mxiter = 50
# Maximum number of inner iterations. (default is 30)
iter1 = 30
# Flag used to select the matrix conditioning method. (default is 1). specify npcond = 1 for
#   modified incomplete cholesky. specify npcond = 2 for polynomial.
npcond = 1
# Is the head change criterion for convergence. (default is 1e-5).
hclose = 1e-05
# Is the residual criterion for convergence. (default is 1e-5)
rclose = 1e-05
# Is the relaxation parameter used with npcond = 1. (default is 1.0)
relax = 1.0
# Is only used when npcond = 2 to indicate whether the estimate of the upper bound on the maximum
#   eigenvalue is 2.0, or whether the estimate will be calculated. nbpol = 2 is used to specify the
#   value is 2.0; for any other value of nbpol, the estimate is calculated. convergence is
#   generally insensitive to this parameter. (default is 0).
nbpol = 0
# Solver print out interval. (default is 0).
iprpcg = 0
# If mutpcg = 0, tables of maximum head change and residual will be printed each iteration. if
#   mutpcg = 1, only the total number of iterations will be printed. if mutpcg = 2, no information
#   will be printed. if mutpcg = 3, information will only be printed if convergence fails. (default
#   is 3).
mutpcg = 3
# Is the steady-state damping factor. (default is 1.)
damp = 1.0
# Is the transient damping factor. (default is 1.)
dampt = 1.0
# Is a flag that determines what happens to an active cell that is surrounded by dry cells.
#   (default is 0). if ihcofadd=0, cell converts to dry regardless of hcof value. this is the
#   default, which is the way pcg2 worked prior to the addition of this option. if ihcofadd<>0,
#   cell converts to dry only if hcof has no head-dependent stresses or storage terms.
ihcofadd = 0

pcg = flopy.modflow.mfpcg.ModflowPcg(model=model, mxiter=mxiter, iter1=iter1, npcond=npcond,
                                     hclose=hclose, rclose=rclose, relax=relax, nbpol=nbpol,
                                     iprpcg=iprpcg, mutpcg=mutpcg, damp=damp, dampt=dampt,
                                     ihcofadd=ihcofadd)
```

## pcgn


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# The maximum number of picard (outer) iterations allowed. for nonlinear problems, this variable
#   must be set to some number greater than one, depending on the problem size and degree of
#   nonlinearity. if iter_mo is set to 1, then the pcgn solver assumes that the problem is linear
#   and the input requirements are greatly truncated. (default is 50)
iter_mo = 50
# Maximum number of pcg (inner) iterations allowed. generally, this variable is set to some number
#   greater than one, depending on the matrix size, degree of convergence called for, and the
#   nature of the problem. for a nonlinear problem, iter_mi should be set large enough that the pcg
#   iteration converges freely with the relative convergence parameter epsilon described in the
#   parameters related to convergence of inner iteration: line 4 subsection. (default is 30)
iter_mi = 30
# The residual-based stopping criterion for iteration. this parameter is used differently,
#   depending on whether it is applied to a linear or nonlinear problem.
close_r = 1e-05
# Close_h is used as an alternate stopping criterion for the picard iteration needed to solve a
#   nonlinear problem. the maximum value of the head change is obtained for each picard iteration,
#   after completion of the inner, pcg iteration. if this maximum head change is less than close_h,
#   then the picard iteration is considered tentatively to have converged. however, as nonlinear
#   problems can demonstrate oscillation in the head solution, the picard iteration is not declared
#   to have converged unless the maximum head change is less than close_h for three picard
#   iterations. if these picard iterations are sequential, then a good solution is assumed to have
#   been obtained. if the picard iterations are not sequential, then a warning is issued advising
#   that the convergence is conditional and the user is urged to examine the mass balance of the
#   solution.
close_h = 1e-05
# Is the relaxation parameter used with npcond = 1. (default is 1.0)
relax = 1.0
# Is the fill level of the mic preconditioner. preconditioners with fill levels of 0 and 1 are
#   available (ifill = 0 and ifill = 1, respectively). (default is 0)
ifill = 0
# Is the unit number of an optional output file where progress for the inner pcg iteration can be
#   written. (default is 0)
unit_pc = 0
# Is the unit number of an optional output file where the actual time in the pcg solver is
#   accumulated. (default is 0)
unit_ts = 0
# Defines the mode of damping applied to the linear solution. in general, damping determines how
#   much of the head changes vector shall be applied to the hydraulic head vector hj in picard
#   iteration j. if adamp = 0, ordinary damping is employed and a constant value of damping
#   parameter will be used throughout the picard iteration; this option requires a valid value for
#   damp. if adamp = 1, adaptive damping is employed. if adamp = 2: enhanced damping algorithm in
#   which the damping value is increased (but never decreased) provided the picard iteration is
#   proceeding satisfactorily. (default is 0)
adamp = 0
# Is the damping factor. (default is 1.)
damp = 1.0
# Is the lower bound placed on the dampening; generally, 0 < damp_lb < damp. (default is 0.001)
damp_lb = 0.001
# Is a rate parameter; generally, 0 < rate_d < 1. (default is 0.1)
rate_d = 0.1
# This variable limits the maximum head change applicable to the updated hydraulic heads in a
#   picard iteration. if chglimit = 0.0, then adaptive damping proceeds without this feature.
#   (default is 0.)
chglimit = 0.0
# Defines the mode of convergence applied to the pcg solver. (default is 0)
acnvg = 0
# Is the minimum value that the relative convergence is allowed to take under the self-adjusting
#   convergence option. cnvg_lb is used only in convergence mode acnvg = 1. (default is 0.001)
cnvg_lb = 0.001
# Increases the relative pcg convergence criteria by a power equal to mcnvg. mcnvg is used only in
#   convergence mode acnvg = 2. (default is 2)
mcnvg = 2
# This option results in variable enhancement of epsilon. if 0 < rate_c < 1, then enhanced relative
#   convergence is allowed to decrease by increasing epsilon(j) = epsilon(j-1) + rate_c
#   epsilon(j-1), where j is the picard iteration number; this change in epsilon occurs so long as
#   the picard iteration is progressing satisfactorily. if rate_c <= 0, then the value of epsilon
#   set by mcnvg remains unchanged through the picard iteration. it should be emphasized that
#   rate_c must have a value greater than 0 for the variable enhancement to be effected; otherwise
#   epsilon remains constant. rate_c is used only in convergence mode acnvg = 2. (default is -1.)
rate_c = -1.0
# Enables progress reporting for the picard iteration. if ipunit >= 0, then a record of progress
#   made by the picard iteration for each time step is printed in the modflow listing file
#   (harbaugh and others, 2000). this record consists of the total number of dry cells at the end
#   of each time step as well as the total number of pcg iterations necessary to obtain
#   convergence. in addition, if ipunit > 0, then extensive diagnostics for each picard iteration
#   is also written in comma-separated format to a file whose unit number corresponds to ipunit;
#   the name for this file, along with its unit number and type 'data' should be entered in the
#   modflow name file. if ipunit < 0 then printing of all progress concerning the picard iteration
#   is suppressed, as well as information on the nature of the convergence of the picard iteration.
#   (default is 0)
ipunit = -1

pcgn = flopy.modflow.mfpcgn.ModflowPcgn(model=model, iter_mo=iter_mo, iter_mi=iter_mi,
                                        close_r=close_r, close_h=close_h, relax=relax, ifill=ifill,
                                        unit_pc=unit_pc, unit_ts=unit_ts, adamp=adamp, damp=damp,
                                        damp_lb=damp_lb, rate_d=rate_d, chglimit=chglimit,
                                        acnvg=acnvg, cnvg_lb=cnvg_lb, mcnvg=mcnvg, rate_c=rate_c,
                                        ipunit=ipunit)
```

## nwt


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Is the maximum head change between outer iterations for solution of the nonlinear problem.
#   (default is 1e-4).
headtol = 0.01
# Is the maximum l2 norm for solution of the nonlinear problem. (default is 500).
fluxtol = 500
# Is the maximum number of iterations to be allowed for solution of the outer (nonlinear) problem.
#   (default is 100).
maxiterout = 100
# Is the portion of the cell thickness (length) used for smoothly adjusting storage and conductance
#   coefficients to zero. (default is 1e-5).
thickfact = 1e-05
# Is a flag that determines which matrix solver will be used. a value of 1 indicates gmres will be
#   used a value of 2 indicates xmd will be used. (default is 1).
linmeth = 1
# Is a flag that indicates whether additional information about solver convergence will be printed
#   to the main listing file. (default is 0).
iprnwt = 0
ibotav = 0
# Specified indicates that the optional solver input values listed for items 1 and 2 will be
#   specified in the nwt input file by the user. simple indicates that default solver input values
#   will be defined that work well for nearly linear models. this would be used for models that do
#   not include nonlinear stress packages, and models that are either confined or consist of a
#   single unconfined layer that is thick enough to contain the water table within a single layer.
#   moderate indicates that default solver input values will be defined that work well for
#   moderately nonlinear models. this would be used for models that include nonlinear stress
#   packages, and models that consist of one or more unconfined layers. the moderate option should
#   be used when the simple option does not result in successful convergence. complex indicates
#   that default solver input values will be defined that work well for highly nonlinear models.
#   this would be used for models that include nonlinear stress packages, and models that consist
#   of one or more unconfined layers representing complex geology and sw/gw interaction. the
#   complex option should be used when the moderate option does not result in successful
#   convergence. (default is complex).
options = 'COMPLEX'
# If the model fails to converge during a time step then it will continue to solve the following
#   time step. (default is false).  note the capital c on this option so that it doesn't conflict
#   with a reserved python language word.
Continue = False
# Is a coefficient used to reduce the weight applied to the head change between nonlinear
#   iterations. dbdtheta is used to control oscillations in head. values range between 0.0 and 1.0,
#   and larger values increase the weight (decrease under-relaxation) applied to the head change.
#   (default is 0.4).
dbdtheta = 0.4
# Is a coefficient used to increase the weight applied to the head change between nonlinear
#   iterations. dbdkappa is used to control oscillations in head. values range between 0.0 and 1.0,
#   and larger values increase the weight applied to the head change. (default is 1.e-5).
dbdkappa = 1e-05
# Is a factor (used to weight the head change for the previous and current iteration. values range
#   between 0.0 and 1.0, and greater values apply more weight to the head change calculated during
#   the current iteration. (default is 0.)
dbdgamma = 0.0
# Is the momentum coefficient and ranges between 0.0 and 1.0. greater values apply more weight to
#   the head change for the current iteration. (default is 0.1).
momfact = 0.1
# Is a flag used to specify whether residual control will be used. a value of 1 indicates that
#   residual control is active and a value of 0 indicates residual control is inactive. (default is
#   1).
backflag = 1
# Is the maximum number of reductions (backtracks) in the head change between nonlinear iterations
#   (integer). a value between 10 and 50 works well. (default is 50).
maxbackiter = 50
# Is the proportional decrease in the root-mean-squared error of the groundwater- flow equation
#   used to determine if residual control is required at the end of a nonlinear iteration. (default
#   is 1.1).
backtol = 1.1
# Is a reduction factor used for residual control that reduces the head change between nonlinear
#   iterations. values should be between 0.0 and 1.0, where smaller values result in smaller
#   head-change values. (default 0.7).
backreduce = 0.7
# (gmres) is the maximum number of iterations for the linear solution. (default is 50).
maxitinner = 50
# (gmres) is the index for selection of the method for incomplete factorization (ilu) used as a
#   preconditioner. (default is 2).
ilumethod = 2
# (gmres) is the fill limit for ilumethod = 1 and is the level of fill for ilumethod = 2.
#   recommended values: 5-10 for method 1, 0-2 for method 2. (default is 5).
levfill = 5
# (gmres) is the tolerance for convergence of the linear solver. this is the residual of the linear
#   equations scaled by the norm of the root mean squared error. usually 1.e-8 to 1.e-12 works
#   well. (default is 1.e-10).
stoptol = 1e-10
# (gmres) is the number of iterations between restarts of the gmres solver. (default is 15).
msdr = 15
# (xmd) is a flag for the acceleration method: 0 is conjugate gradient, 1 is orthomin, 2 is
#   bi-cgstab. (default is 2).
iacl = 2
# (xmd) is a flag for the scheme of ordering the unknowns: 0 is original ordering, 1 is rcm
#   ordering, 2 is minimum degree ordering. (default is 1).
norder = 1
# (xmd) is the level of fill for incomplete lu factorization. (default is 5).
level = 5
# (xmd) is the number of orthogonalization for the orthomin acceleration scheme. a number between 4
#   and 10 is appropriate. small values require less storage but more iterations may be required.
#   this number should equal 2 for the other acceleration methods. (default is 7).
north = 7
# (xmd) is a flag for reduced system preconditioning (integer): 0-do not apply reduced system
#   preconditioning, 1-apply reduced system preconditioning. (default is 0)
iredsys = 0
# (xmd) is the residual reduction-convergence criteria. (default is 0.).
rrctols = 0.0
# (xmd) is a flag for using drop tolerance in the preconditioning: 0-don't use drop tolerance,
#   1-use drop tolerance. (default is 1).
idroptol = 1
# (xmd) is the drop tolerance for preconditioning. (default is 1.e-4).
epsrn = 0.0001
# (xmd) is the head closure criteria for inner (linear) iterations. (default is 1.e-4).
hclosexmd = 0.0001
# (xmd) is the maximum number of iterations for the linear solution. (default is 50).
mxiterxmd = 50

nwt = flopy.modflow.mfnwt.ModflowNwt(model=model, headtol=headtol, fluxtol=fluxtol,
                                     maxiterout=maxiterout, thickfact=thickfact, linmeth=linmeth,
                                     iprnwt=iprnwt, ibotav=ibotav, options=options,
                                     Continue=Continue, dbdtheta=dbdtheta, dbdkappa=dbdkappa,
                                     dbdgamma=dbdgamma, momfact=momfact, backflag=backflag,
                                     maxbackiter=maxbackiter, backtol=backtol,
                                     backreduce=backreduce, maxitinner=maxitinner,
                                     ilumethod=ilumethod, levfill=levfill, stoptol=stoptol,
                                     msdr=msdr, iacl=iacl, norder=norder, level=level, north=north,
                                     iredsys=iredsys, rrctols=rrctols, idroptol=idroptol,
                                     epsrn=epsrn, hclosexmd=hclosexmd, mxiterxmd=mxiterxmd)
```

## pks


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Maximum number of outer iterations. (default is 100)
mxiter = 100
# Maximum number of inner iterations. (default is 30)
innerit = 50
isolver = 1
npc = 2
iscl = 0
iord = 0
ncoresm = 1
ncoresv = 1
# Is the steady-state damping factor. (default is 1.)
damp = 1.0
# Is the transient damping factor. (default is 1.)
dampt = 1.0
# Is the relaxation parameter used with npcond = 1. (default is 1.0)
relax = 0.97
ifill = 0
droptol = 0.0
# Is the head change criterion for convergence. (default is 1.e-3).
hclose = 0.001
# Is the residual criterion for convergence. (default is 1.e-1)
rclose = 0.1
l2norm = None
# Solver print out interval. (default is 0).
iprpks = 0
# If mutpcg = 0, tables of maximum head change and residual will be printed each iteration. if
#   mutpcg = 1, only the total number of iterations will be printed. if mutpcg = 2, no information
#   will be printed. if mutpcg = 3, information will only be printed if convergence fails. (default
#   is 3).
mutpks = 3
mpi = False
partopt = 0
novlapimpsol = 1
stenimpsol = 2
verbose = 0
partdata = None

pks = flopy.modflow.mfpks.ModflowPks(model=model, mxiter=mxiter, innerit=innerit, isolver=isolver,
                                     npc=npc, iscl=iscl, iord=iord, ncoresm=ncoresm,
                                     ncoresv=ncoresv, damp=damp, dampt=dampt, relax=relax,
                                     ifill=ifill, droptol=droptol, hclose=hclose, rclose=rclose,
                                     l2norm=l2norm, iprpks=iprpks, mutpks=mutpks, mpi=mpi,
                                     partopt=partopt, novlapimpsol=novlapimpsol,
                                     stenimpsol=stenimpsol, verbose=verbose, partdata=partdata)
```

## sms


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Is the head change criterion for convergence of the outer (nonlinear) iterations, in units of
#   length. when the maximum absolute value of the head change at all nodes during an iteration is
#   less than or equal to hclose, iteration stops. commonly, hclose equals 0.01.
hclose = 0.0001
# Is the head change criterion for convergence of the inner (linear) iterations, in units of
#   length. when the maximum absolute value of the head change at all nodes during an iteration is
#   less than or equal to hiclose, the matrix solver assumes convergence. commonly, hiclose is set
#   an order of magnitude less than hclose.
hiclose = 0.0001
# Is the maximum number of outer (nonlinear) iterations -- that is, calls to the solution routine.
#   for a linear problem mxiter should be 1.
mxiter = 100
# Is the maximum number of inner (linear) iterations. the number typically depends on the
#   characteristics of the matrix solution scheme being used. for nonlinear problems, iter1 usually
#   ranges from 60 to 600; a value of 100 will be sufficient for most linear problems.
iter1 = 20
# Is a flag that controls printing of convergence information from the solver: 0 is print nothing;
#   1 is print only the total number of iterations and nonlinear residual reduction summaries;  2
#   is print matrix solver information in addition to above.
iprsms = 2
# Is a flag that controls the nonlinear solution method and under- relaxation schemes. 0 is picard
#   iteration scheme is used without any under-relaxation schemes involved. > 0 is newton-raphson
#   iteration scheme is used with under-relaxation. note that the newton-raphson linearization
#   scheme is available only for the upstream weighted solution scheme of the bcf and lpf packages.
#   < 0 is picard iteration scheme is used with under-relaxation. the absolute value of nonlinmeth
#   determines the underrelaxation scheme used. 1 or -1, then delta-bar-delta under-relaxation is
#   used. 2 or -2 then cooley under-relaxation scheme is used. note that the under-relaxation
#   schemes are used in conjunction with gradient based methods, however, experience has indicated
#   that the cooley under-relaxation and damping work well also for the picard scheme with the
#   wet/dry options of modflow.
nonlinmeth = 0
# Is a flag that controls the matrix solution method. 1 is the xmd solver of ibaraki (2005). 2 is
#   the unstructured pre-conditioned conjugate gradient solver of white and hughes (2011).
linmeth = 2
# Is the reduction factor for the learning rate (under-relaxation term) of the delta-bar-delta
#   algorithm. the value of theta is between zero and one. if the change in the variable (head) is
#   of opposite sign to that of the previous iteration, the under-relaxation term is reduced by a
#   factor of theta. the value usually ranges from 0.3 to 0.9; a value of 0.7 works well for most
#   problems.
theta = 0.7
# Is the increment for the learning rate (under-relaxation term) of the delta-bar-delta algorithm.
#   the value of akappa is between zero and one. if the change in the variable (head) is of the
#   same sign to that of the previous iteration, the under-relaxation term is increased by an
#   increment of akappa. the value usually ranges from 0.03 to 0.3; a value of 0.1 works well for
#   most problems.
akappa = 0.1
# Is the history or memory term factor of the delta-bar-delta algorithm. gamma is between zero and
#   1 but cannot be equal to one. when gamma is zero, only the most recent history (previous
#   iteration value) is maintained. as gamma is increased, past history of iteration changes has
#   greater influence on the memory term.  the memory term is maintained as an exponential average
#   of past changes. retaining some past history can overcome granular behavior in the calculated
#   function surface and therefore helps to overcome cyclic patterns of non-convergence. the value
#   usually ranges from 0.1 to 0.3; a value of 0.2 works well for most problems.
gamma = 0.2
# Is the fraction of past history changes that is added as a momentum term to the step change for a
#   nonlinear iteration. the value of amomentum is between zero and one. a large momentum term
#   should only be used when small learning rates are expected. small amounts of the momentum term
#   help convergence. the value usually ranges from 0.0001 to 0.1; a value of 0.001 works well for
#   most problems.
amomentum = 0.001
# Is the maximum number of backtracking iterations allowed for residual reduction computations. if
#   numtrack = 0 then the backtracking iterations are omitted. the value usually ranges from 2 to
#   20; a value of 10 works well for most problems.
numtrack = 20
# Is the tolerance for residual change that is allowed for residual reduction computations. btol
#   should not be less than one to avoid getting stuck in local minima. a large value serves to
#   check for extreme residual increases, while a low value serves to control step size more
#   severely. the value usually ranges from 1.0 to 1e6 ; a value of 1e4 works well for most
#   problems but lower values like 1.1 may be required for harder problems.
btol = 10000.0
breduc = 0.2
# Is the limit to which the residual is reduced with backtracking. if the residual is smaller than
#   reslim, then further backtracking is not performed. a value of 100 is suitable for large
#   problems and residual reduction to smaller values may only slow down computations.
reslim = 100.0
# Is the flag for choosing the acceleration method. 0 is conjugate gradient; select this option if
#   the matrix is symmetric. 1 is orthomin. 2 is bicgstab.
iacl = 2
# Is the flag for choosing the ordering scheme. 0 is original ordering 1 is reverse cuthill mckee
#   ordering 2 is minimum degree ordering
norder = 0
# Is the level of fill for ilu decomposition. higher levels of fill provide more robustness but
#   also require more memory. for optimal performance, it is suggested that a large level of fill
#   be applied (7 or 8) with use of drop tolerance.
level = 7
# Is the number of orthogonalizations for the orthomin acceleration scheme. a number between 4 and
#   10 is appropriate. small values require less storage but more iteration may be required. this
#   number should equal 2 for the other acceleration methods.
north = 2
# Is the index for creating a reduced system of equations using the red-black ordering scheme. 0 is
#   do not create reduced system 1 is create reduced system using red-black ordering
iredsys = 0
# Is a residual tolerance criterion for convergence. the root mean squared residual of the matrix
#   solution is evaluated against this number to determine convergence. the solver assumes
#   convergence if either hiclose (the absolute head tolerance value for the solver) or rrctol is
#   achieved. note that a value of zero ignores residual tolerance in favor of the absolute
#   tolerance (hiclose) for closure of the matrix solver.
rrctol = 0.0
# Is the flag to perform drop tolerance. 0 is do not perform drop tolerance 1 is perform drop
#   tolerance
idroptol = 0
# Is the drop tolerance value. a value of 1e-3 works well for most problems.
epsrn = 0.001
# An option keyword that defines the linear acceleration method used by the pcgu solver. clin is
#   "cg", then preconditioned conjugate gradient method. clin is "bcgs", then preconditioned
#   bi-conjugate gradient stabilized method.
clin = 'bcgs'
# An integer value that defines the preconditioner. ipc = 0, no preconditioning. ipc = 1, jacobi
#   preconditioning. ipc = 2, ilu(0) preconditioning. ipc = 3, milu(0) preconditioning (default).
ipc = 3
# Is the flag for choosing the matrix scaling approach used. 0 is no matrix scaling applied 1 is
#   symmetric matrix scaling using the scaling method by the polcg preconditioner in hill (1992). 2
#   is symmetric matrix scaling using the l2 norm of each row of a (dr) and the l2 norm of each row
#   of dra.
iscl = 0
# Is the flag for choosing the matrix reordering approach used. 0 = original ordering 1 = reverse
#   cuthill mckee ordering 2 = minimum degree ordering
iord = 0
# A real value that defines the flow residual tolerance for convergence of the pcgu linear solver.
#   this value represents the maximum allowable residual at any single node. value is in units of
#   length cubed per time, and must be consistent with modflow-usg length and time units. usually a
#   value of 1.0x10-1 is sufficient for the flow-residual criteria when meters and seconds are the
#   defined modflow-usg length and time.
rclosepcgu = 0.1
# A real value that defines the relaxation factor used by the milu(0) preconditioner. relaxpcgu is
#   unitless and should be greater than or equal to 0.0 and less than or equal to 1.0. relaxpcgu
#   values of about 1.0 are commonly used, and experience suggests that convergence can be
#   optimized in some cases with relaxpcgu values of 0.97. a relaxpcgu value of 0.0 will result in
#   ilu(0) preconditioning. relaxpcgu is only specified if ipc=3. if relaxpcgu is not specified and
#   ipc=3, then a default value of 0.97 will be assigned to relaxpcgu.
relaxpcgu = 1.0
options = []

sms = flopy.modflow.mfsms.ModflowSms(model=model, hclose=hclose, hiclose=hiclose, mxiter=mxiter,
                                     iter1=iter1, iprsms=iprsms, nonlinmeth=nonlinmeth,
                                     linmeth=linmeth, theta=theta, akappa=akappa, gamma=gamma,
                                     amomentum=amomentum, numtrack=numtrack, btol=btol,
                                     breduc=breduc, reslim=reslim, iacl=iacl, norder=norder,
                                     level=level, north=north, iredsys=iredsys, rrctol=rrctol,
                                     idroptol=idroptol, epsrn=epsrn, clin=clin, ipc=ipc, iscl=iscl,
                                     iord=iord, rclosepcgu=rclosepcgu, relaxpcgu=relaxpcgu,
                                     options=options)
```

## lak


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
nlakes = 1
ipakcb = None
theta = -1.0
nssitr = 0
sscncr = 0.0
surfdep = 0.0
stages = 1.0
stage_range = None
tab_files = None
tab_units = None
lakarr = None
bdlknc = None
sill_data = None
flux_data = None
# Package options. (default is none).
options = None

lak = flopy.modflow.mflak.ModflowLak(model=model, nlakes=nlakes, ipakcb=ipakcb, theta=theta,
                                     nssitr=nssitr, sscncr=sscncr, surfdep=surfdep, stages=stages,
                                     stage_range=stage_range, tab_files=tab_files,
                                     tab_units=tab_units, lakarr=lakarr, bdlknc=bdlknc,
                                     sill_data=sill_data, flux_data=flux_data, options=options)
```

## gage


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# The total number of gages included in the gage file (default is 0).
numgage = 0
# Data for dataset 2a and 2b in the gage package. if a list is provided then the list includes 2 to
#   3 entries (lake unit [outtype]) for each lak package entry and 4 entries (gageseg gagerch unit
#   outtype) for each sfr package entry. if a numpy array it passed each gage location must have 4
#   entries, where lak package gages can have any value for the second column. the numpy array can
#   be created using the get_empty() method available in modflowgage. default is none
gage_data = None
# Names of gage output files. a file name must be provided for each gage. if files are not provided
#   and filenames=none then a gage name will be created using the model name and the gage number
#   (for example, modflowtest.gage1.go). default is none.
files = None

gage = flopy.modflow.mfgage.ModflowGage(model=model, numgage=numgage, gage_data=gage_data,
                                        files=files)
```

## sip


```python
# The model object (of type :class:flopy.modflow.mf.modflow) to which this package will be added.
model = modflow
# The maximum number of times through the iteration loop in one time step in an attempt to solve
#   the system of finite-difference equations. (default is 200)
mxiter = 200
# The number of iteration variables to be used. five variables are generally sufficient. (default
#   is 5)
nparm = 5
# The acceleration variable, which must be greater than zero and is generally equal to one. if a
#   zero is entered, it is changed to one. (default is 1)
accl = 1
# The head change criterion for convergence. when the maximum absolute value of head change from
#   all nodes during an iteration is less than or equal to hclose, iteration stops. (default is
#   1e-5)
hclose = 1e-05
# A flag indicating where the seed for calculating iteration variables will come from. 0 is the
#   seed entered by the user will be used. 1 is the seed will be calculated at the start of the
#   simulation from problem variables. (default is 0)
ipcalc = 1
# The seed for calculating iteration variables. wseed is always read, but is used only if ipcalc is
#   equal to zero. (default is 0)
wseed = 0
# The printout interval for sip. iprsip, if equal to zero, is changed to 999. the maximum head
#   change (positive or negative) is printed for each iteration of a time step whenever the time
#   step is an even multiple of iprsip. this printout also occurs at the end of each stress period
#   regardless of the value of iprsip. (default is 0)
iprsip = 0

sip = flopy.modflow.mfsip.ModflowSip(model=model, mxiter=mxiter, nparm=nparm, accl=accl,
                                     hclose=hclose, ipcalc=ipcalc, wseed=wseed, iprsip=iprsip)
```

## sor


```python
# The model object (of type :class:flopy.modflow.mf.modflow) to which this package will be added.
model = modflow
# The maximum number of iterations allowed in a time step. (default is 200)
mxiter = 200
# The acceleration variable, which must be greater than zero and is generally between 1. and 2.
#   (default is 1)
accl = 1
# The head change criterion for convergence. when the maximum absolute value of head change from
#   all nodes during an iteration is less than or equal to hclose, iteration stops. (default is
#   1e-5)
hclose = 1e-05
# The printout interval for sor. iprsor, if equal to zero, is changed to 999. the maximum head
#   change (positive or negative) is printed for each iteration of a time step whenever the time
#   step is an even multiple of iprsor. this printout also occurs at the end of each stress period
#   regardless of the value of iprsor. (default is 0)
iprsor = 0

sor = flopy.modflow.mfsor.ModflowSor(model=model, mxiter=mxiter, accl=accl, hclose=hclose,
                                     iprsor=iprsor)
```

## de4


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Maximum number of iterations for each time step. specify itmax = 1 if  iteration is not desired.
#   ideally iteration would not be required for  direct solution. however, it is necessary to
#   iterate if the flow  equation is nonlinear or if computer precision limitations result in
#   inaccurate calculations as indicated by a large water budget error  (default is 50).
itmx = 50
# Maximum number of equations in the upper part of the equations to be  solved. this value impacts
#   the amount of memory used by the de4  package. if specified as 0, the program will calculate
#   mxup as half  the number of cells in the model, which is an upper limit (default  is 0).
mxup = 0
# Maximum number of equations in the lower part of equations to be  solved. this value impacts the
#   amount of memory used by the de4  package. if specified as 0, the program will calculate mxlow
#   as half  the number of cells in the model, which is an upper limit (default is  0).
mxlow = 0
# Maximum band width plus 1 of the lower part of the head coefficients  matrix. this value impacts
#   the amount of memory used by the de4  package. if specified as 0, the program will calculate
#   mxbw as the  product of the two smallest grid dimensions plus 1, which is an  upper limit
#   (default is 0).
mxbw = 0
# Flag indicating the frequency at which coefficients in head matrix  change. ifreq = 1 indicates
#   that the flow equations are linear and that  coefficients of simulated head for all stress
#   terms are constant  for all stress periods.  ifreq = 2 indicates that the flow equations are
#   linear, but  coefficients of simulated head for some stress terms may change  at the start of
#   each stress period. ifreq = 3 indicates that a nonlinear flow equation is being solved,  which
#   means that some terms in the head coefficients matrix depend  on simulated head (default is 3).
ifreq = 3
# Flag that indicates the quantity of information that is printed when  convergence information is
#   printed for a time step. mutd4 = 0 indicates that the number of iterations in the time step
#   and the maximum head change each iteration are printed. mutd4 = 1 indicates that only the
#   number of iterations in the time  step is printed. mutd4 = 2 indicates no information is
#   printed (default is 0).
mutd4 = 0
# Multiplier for the computed head change for each iteration. normally  this value is 1. a value
#   greater than 1 may be useful for improving  the rate of convergence when using external
#   iteration to solve  nonlinear problems (default is 1).
accl = 1.0
# Head change closure criterion. if iterating (itmx > 1), iteration  stops when the absolute value
#   of head change at every node is less  than or equal to hclose. hclose is not used if not
#   iterating, but a  value must always be specified (default is 1e-5).
hclose = 1e-05
# Time step interval for printing out convergence information when  iterating (itmx > 1). if iprd4
#   is 2, convergence information is  printed every other time step. a value must always be
#   specified  even if not iterating (default is 1).
iprd4 = 1

de4 = flopy.modflow.mfde4.ModflowDe4(model=model, itmx=itmx, mxup=mxup, mxlow=mxlow, mxbw=mxbw,
                                     ifreq=ifreq, mutd4=mutd4, accl=accl, hclose=hclose,
                                     iprd4=iprd4)
```

## oc


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Is a code for the format in which heads will be printed. (default is 0).
ihedfm = 0
# Is a code for the format in which heads will be printed. (default is 0).
iddnfm = 0
# Is a character value that specifies the format for saving heads. the format must contain 20
#   characters or less and must be a valid fortran format that is enclosed in parentheses. the
#   format must be enclosed in apostrophes if it contains one or more blanks or commas. the
#   optional word label after the format is used to indicate that each layer of output should be
#   preceded with a line that defines the output (simulation time, the layer being output, and so
#   forth). if there is no record specifying chedfm, then heads are written to a binary
#   (unformatted) file. binary files are usually more compact than text files, but they are not
#   generally transportable among different computer operating systems or different fortran
#   compilers. (default is none)
chedfm = None
# Is a character value that specifies the format for saving drawdown. the format must contain 20
#   characters or less and must be a valid fortran format that is enclosed in parentheses. the
#   format must be enclosed in apostrophes if it contains one or more blanks or commas. the
#   optional word label after the format is used to indicate that each layer of output should be
#   preceded with a line that defines the output (simulation time, the layer being output, and so
#   forth). if there is no record specifying cddnfm, then drawdowns are written to a binary
#   (unformatted) file. binary files are usually more compact than text files, but they are not
#   generally transportable among different computer operating systems or different fortran
#   compilers. (default is none)
cddnfm = None
# Is a character value that specifies the format for saving ibound. the format must contain 20
#   characters or less and must be a valid fortran format that is enclosed in parentheses. the
#   format must be enclosed in apostrophes if it contains one or more blanks or commas. the
#   optional word label after the format is used to indicate that each layer of output should be
#   preceded with a line that defines the output (simulation time, the layer being output, and so
#   forth). if there is no record specifying cboufm, then ibounds are written to a binary
#   (unformatted) file. binary files are usually more compact than text files, but they are not
#   generally transportable among different computer operating systems or different fortran
#   compilers. (default is none)
cboufm = None
# Save results in compact budget form. (default is true).
compact = True
# Dictionary key is a tuple with the zero-based period and step  (iperoc, itsoc) for each
#   print/save option list.  (default is {(0,0):['save head']})  the list can have any valid
#   modflow oc print/save option:     print head     print drawdown     print budget     save head
#   save drawdown     save budget     save ibound          the lists can also include (1)
#   ddreference in the list to reset      drawdown reference to the period and step and (2) a list
#   of layers      for print head, save head, print drawdown, save drawdown, and     save ibound.
#   the list is used for every stress period and time step after the  (iperoc, itsoc) tuple until a
#   (iperoc, itsoc) tuple is entered with and empty list.
stress_period_data = {(0, 0): ['save head']}

oc = flopy.modflow.mfoc.ModflowOc(model=model, ihedfm=ihedfm, iddnfm=iddnfm, chedfm=chedfm,
                                  cddnfm=cddnfm, cboufm=cboufm, compact=compact,
                                  stress_period_data=stress_period_data)
```

## uzf


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Used to define which cell in a vertical column that recharge and discharge is simulated. (default
#   is 1)
nuztop = 1
# Equal to 1 or 2. a value of 1 indicates that the vertical hydraulic conductivity will be
#   specified within the uzf1 package input file using array vks. a value of 2 indicates that the
#   vertical hydraulic conductivity will be specified within either the bcf or lpf package input
#   file. (default is 0)
iuzfopt = 0
# Specifies whether ground water that discharges to land surface will be routed to stream segments
#   or lakes as specified in the irunbnd array (irunflg not equal to zero) or if ground-water
#   discharge is removed from the model simulation and accounted for in the ground-water budget as
#   a loss of water (irunflg=0). the streamflow-routing (sfr2) and(or) the lake (lak3) packages
#   must be active if irunflg is not zero. (default is 0)
irunflg = 0
# Specifies whether or not evapotranspiration (et) will be simulated. et will not be simulated if
#   ietflg is zero, otherwise it will be simulated. (default is 0)
ietflg = 0
# Flag for writing ground-water recharge, et, and ground-water discharge to land surface rates to a
#   separate unformatted file using subroutine ubudsv. if ipakcb>0, it is the unit number to which
#   the cell-by-cell rates will be written when 'save budget' or a non-zero value for icbcfl is
#   specified in output control. if ipakcb less than or equal to 0, cell-by-cell rates will not be
#   written to a file. (default is 57)
ipakcb = 0
# Flag for writing ground-water recharge, et, and ground-water discharge to land surface rates to a
#   separate unformatted file using module ubdsv3. if iuzfcb2>0, it is the unit number to which
#   cell-by-cell rates will be written when 'save budget' or a non-zero value for icbcfl is
#   specified in output control. if iuzfcb2 less than or equal to 0, cell-by-cell rates will not be
#   written to file. (default is 0)
iuzfcb2 = 0
# Equal to the number of trailing waves used to define the water-content profile following a
#   decrease in the infiltration rate. the number of trailing waves varies depending on the
#   problem, but a range between 10 and 20 is usually adequate. more trailing waves may decrease
#   mass-balance error and will increase computational requirements and memory usage. (default is
#   10)
ntrail2 = 10
# Equal to the number of wave sets used to simulate multiple infiltration periods. the number of
#   wave sets should be set to 20 for most problems involving time varying infiltration. the total
#   number of waves allowed within an unsaturated zone cell is equal to ntrail2*nsets2. an error
#   will occur if the number of waves in a cell exceeds this value. (default is 20)
nsets = 20
# Equal to the number of cells (one per vertical column) that will be specified for printing
#   detailed information on the unsaturated zone water budget and water content. a gage also may be
#   used to print the budget summed over all model cells.  (default is 0)
nuzgag = 0
# The average height of undulations, d (figure 1 in uzf documentation), in the land surface
#   altitude. (default is 1.0)
surfdep = 1.0
# Used to define the aerial extent of the active model in which recharge and discharge will be
#   simulated. (default is 1)
iuzfbnd = 1
# Used to define the stream segments within the streamflow-routing (sfr2) package or lake numbers
#   in the lake (lak3) package that overland runoff from excess infiltration and ground-water
#   discharge to land surface will be added. a positive integer value identifies the stream segment
#   and a negative integer value identifies the lake number. (default is 0)
irunbnd = 0
# Used to define the saturated vertical hydraulic conductivity of the unsaturated zone (lt-1).
#   (default is 1.0e-6)
vks = 9.999999974752427e-07
# Values for each model cell used to define the brooks-corey epsilon of the unsaturated zone.
#   epsilon is used in the relation of water content to hydraulic conductivity (brooks and corey,
#   1966). (default is 3.5)
eps = 3.5
# Used to define the saturated water content of the unsaturated zone in units of volume of water to
#   total volume (l3l-3). (default is 0.35)
thts = 0.35
# Used to define the residual water content for each vertical column of cells in units of volume of
#   water to total volume (l3l-3). thtr is the irreducible water content and the unsaturated water
#   content cannot drain to water contents less than thtr. this variable is not included unless the
#   key word specifythtr is specified. (default is 0.15)
thtr = 0.15
# Used to define the initial water content for each vertical column of cells in units of volume of
#   water at start of simulation to total volume (l3l-3). thti should not be specified for
#   steady-state simulations. (default is 0.20)
thti = 0.2
# Key word for specifying optional input variable thtr (default is 0)
specifythtr = 0
# Key word for specifying optional input variable thti. (default is 0)
specifythti = 0
# Key word for inactivating calculation of surface leakage. (default is 0)
nosurfleak = 0
# Used to define the infiltration rates (lt-1) at land surface for each vertical column of cells.
#   if finf is specified as being greater than the vertical hydraulic conductivity then finf is set
#   equal to the vertical unsaturated hydraulic conductivity. excess water is routed to streams or
#   lakes when irunflg is not zero, and if sfr2 or lak3 is active. (default is 1.0e-8)
finf = 9.99999993922529e-09
# Used to define the et demand rates (l1t-1) within the et extinction depth interval for each
#   vertical column of cells. (default is 5.0e-8)
pet = 5e-08
# Used to define the et extinction depths. the quantity of et removed from a cell is limited by the
#   volume of water stored in the unsaturated zone above the extinction depth. if ground water is
#   within the et extinction depth, then the rate removed is based on a linear decrease in the
#   maximum rate at land surface and zero at the et extinction depth. the linear decrease is the
#   same method used in the evapotranspiration package (mcdonald and harbaugh, 1988, chap. 10).
#   (default is 15.0)
extdp = 15.0
# Used to define the extinction water content below which et cannot be removed from the unsaturated
#   zone.  extwc must have a value between (thts-sy) and thts, where sy is the specific yield
#   specified in either the lpf or bcf package. (default is 0.1)
extwc = 0.1
uzgag = None

uzf = flopy.modflow.mfuzf1.ModflowUzf1(model=model, nuztop=nuztop, iuzfopt=iuzfopt,
                                       irunflg=irunflg, ietflg=ietflg, ipakcb=ipakcb,
                                       iuzfcb2=iuzfcb2, ntrail2=ntrail2, nsets=nsets,
                                       nuzgag=nuzgag, surfdep=surfdep, iuzfbnd=iuzfbnd,
                                       irunbnd=irunbnd, vks=vks, eps=eps, thts=thts, thtr=thtr,
                                       thti=thti, specifythtr=specifythtr, specifythti=specifythti,
                                       nosurfleak=nosurfleak, finf=finf, pet=pet, extdp=extdp,
                                       extwc=extwc, uzgag=uzgag)
```

## upw


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# Layer type (default is 0).
laytyp = 0
# Layer average (default is 0). 0 is harmonic mean 1 is logarithmic mean 2 is arithmetic mean of
#   saturated thickness and logarithmic mean of of hydraulic conductivity
layavg = 0
# Contains a value for each layer that is a flag or the horizontal anisotropy. if chani is less
#   than or equal to 0, then variable hani defines horizontal anisotropy. if chani is greater than
#   0, then chani is the horizontal anisotropy for the entire layer, and hani is not read. if any
#   hani parameters are used, chani for all layers must be less than or equal to 0. use as many
#   records as needed to enter a value of chani for each layer. the horizontal anisotropy is the
#   ratio of the hydraulic conductivity along columns (the y direction) to the hydraulic
#   conductivity along rows (the x direction).
chani = 1.0
# A flag for each layer that indicates whether variable vka is vertical hydraulic conductivity or
#   the ratio of horizontal to vertical hydraulic conductivity.
layvka = 0
# Contains a flag for each layer that indicates if wetting is active. laywet should always be zero
#   for the upw package because all cells initially active are wettable.
laywet = 0
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 53)
ipakcb = None
# Is the head that is assigned to cells that are converted to dry during a simulation. although
#   this value plays no role in the model calculations, it is useful as an indicator when looking
#   at the resulting heads that are output from the model. hdry is thus similar to hnoflo in the
#   basic package, which is the value assigned to cells that are no-flow cells at the start of a
#   model simulation. (default is -1.e30).
hdry = -1e+30
# Iphdry is a flag that indicates whether groundwater head will be set to hdry when the groundwater
#   head is less than 0.0001 above the cell bottom (units defined by lenuni in the discretization
#   package). if iphdry=0, then head will not be set to hdry. if iphdry>0, then head will be set to
#   hdry. if the head solution from one simulation will be used as starting heads for a subsequent
#   simulation, or if the observation process is used (harbaugh and others, 2000), then hdry should
#   not be printed to the output file for dry cells (that is, the upw package input variable should
#   be set as iphdry=0). (default is 0)
iphdry = 0
# Is the hydraulic conductivity along rows. hk is multiplied by horizontal anisotropy (see chani
#   and hani) to obtain hydraulic conductivity along columns. (default is 1.0).
hk = 1.0
# Is the ratio of hydraulic conductivity along columns to hydraulic conductivity along rows, where
#   hk of item 10 specifies the hydraulic conductivity along rows. thus, the hydraulic conductivity
#   along columns is the product of the values in hk and hani. (default is 1.0).
hani = 1.0
# Is either vertical hydraulic conductivity or the ratio of horizontal to vertical hydraulic
#   conductivity depending on the value of layvka. (default is 1.0).
vka = 1.0
# Is specific storage unless the storagecoefficient option is used. when storagecoefficient is
#   used, ss is confined storage coefficient. (default is 1.e-5).
ss = 1e-05
# Is specific yield. (default is 0.15).
sy = 0.15
# Is the vertical hydraulic conductivity of a quasi-three-dimensional confining bed below a layer.
#   (default is 0.0).
vkcb = 0.0
# Noparcheck turns off the checking that a value is defined for all cells when parameters are used
#   to define layer data.
noparcheck = False

upw = flopy.modflow.mfupw.ModflowUpw(model=model, laytyp=laytyp, layavg=layavg, chani=chani,
                                     layvka=layvka, laywet=laywet, ipakcb=ipakcb, hdry=hdry,
                                     iphdry=iphdry, hk=hk, hani=hani, vka=vka, ss=ss, sy=sy,
                                     vkcb=vkcb, noparcheck=noparcheck)
```

## sub


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Isuboc is a flag used to control output of information generated by the sub package. (default is
#   0).
isuboc = 0
# Idsave is a flag and a unit number on which restart records for delay interbeds will be saved at
#   the end of the simulation. (default is 0).
idsave = None
# Idrest is a flag and a unit number on which restart records for delay interbeds will be read in
#   at the start of the simulation (default is 0).
idrest = 0
# Nndb is the number of systems of no-delay interbeds. (default is 1).
nndb = 1
# Ndb is the number of systems of delay interbeds. (default is 1).
ndb = 1
# Nmz is the number of material zones that are needed to define the hydraulic properties of systems
#   of delay interbeds. each material zone is defined by a combination of vertical hydraulic
#   conductivity, elastic specific storage, and inelastic specific storage. (default is 1).
nmz = 1
# Nn is the number of nodes used to discretize the half space to approximate the head distributions
#   in systems of delay interbeds. (default is 20).
nn = 20
# Ac1 is an acceleration parameter.  this parameter is used to predict the aquifer head at the
#   interbed boundaries on the basis of the head change computed for the previous iteration. a
#   value of 0.0 results in the use of the aquifer head at the previous iteration. limited
#   experience indicates that optimum values may range from 0.0 to 0.6. (default is 0).
ac1 = 0.0
# Ac2 is an acceleration parameter. this acceleration parameter is a multiplier for the head
#   changes to compute the head at the new iteration. values are normally between 1.0 and 2.0, but
#   the optimum is probably closer to 1.0 than to 2.0. however this parameter also can be used to
#   help convergence of the iterative solution by using values between 0 and 1. (default is 0.2).
ac2 = 0.2
# Itmin is the minimum number of iterations for which one-dimensional equations will be solved for
#   flow in interbeds when the strongly implicit procedure (sip) is used to solve the ground-water
#   flow equations. if the current iteration level is greater than itmin and the sip convergence
#   criterion for head closure (hclose) is met at a particular cell, the one-dimensional equations
#   for that cell will not be solved. the previous solution will be used. the value of itmin is not
#   used if a solver other than sip is used to solve the ground-water flow equations. (default is
#   5).
itmin = 5
# Ln is a one-dimensional array specifying the model layer assignments for each system of no-delay
#   interbeds. (default is 0).
ln = 0
# Ldn is a one-dimensional array specifying the model layer assignments for each system of delay
#   interbeds.(default is 0).
ldn = 0
# Rnb is an array specifying the factor nequiv at each cell for each system of delay interbeds. the
#   array also is used to define the areal extent of each system of interbeds. for cells beyond the
#   areal extent of the system of interbeds, enter a number less than 1.0 in the corresponding
#   element of this array. (default is 1).
rnb = 1.0
# Hc is an array specifying the preconsolidation head or preconsolidation stress in terms of head
#   in the aquifer for systems of no-delay interbeds. for any model cells in which specified hc is
#   greater than the corresponding value of starting head, the value of hc will be set to that of
#   starting head. (default is 100000).
hc = 100000.0
# Sfe is an array specifying the dimensionless elastic skeletal storage coefficient for systems of
#   no-delay interbeds. (default is 1.e-4).
sfe = 9.999999747378752e-05
# Sfv is an array specifying the dimensionless inelastic skeletal storage coefficient for systems
#   of no-delay interbeds. (default is 1.e-3).
sfv = 0.0010000000474974513
# Com is an array specifying the starting compaction in each system of no-delay interbeds.
#   compaction values computed by the package are added to values in this array so that printed or
#   stored values of compaction and land subsidence may include previous components. values in this
#   array do not affect calculations of storage changes or resulting compaction. for simulations in
#   which output values are to reflect compaction and subsidence since the start of the simulation,
#   enter zero values for all elements of this array. (default is 0).
com = 0.0
# Data item includes nmz records, each with a value of vertical hydraulic conductivity, elastic
#   specific storage, and inelastic specific storage. (default is [1.e-6, 6.e-6, 6.e-4]).
dp = np.array([ 0.000001, 0.000006, 0.0006 ])
# Dstart is an array specifying starting head in interbeds for systems of delay interbeds. for a
#   particular location in a system of interbeds, the starting head is applied to every node in the
#   string of nodes that approximates flow in half of a doubly draining interbed. (default is 1).
dstart = 1.0
# Dhc is an array specifying the starting preconsolidation head in interbeds for systems of delay
#   interbeds. for a particular location in a system of interbeds, the starting preconsolidation
#   head is applied to every node in the string of nodes that approximates flow in half of a doubly
#   draining interbed. for any location at which specified starting preconsolidation head is
#   greater than the corresponding value of the starting head, dstart, the value of the starting
#   preconsolidation head will be set to that of the starting head. (default is 100000).
dhc = 100000.0
# Dcom is an array specifying the starting compaction in each system of delay interbeds. compaction
#   values computed by the package are added to values in this array so that printed or stored
#   values of compaction and land subsidence may include previous components. values in this array
#   do not affect calculations of storage changes or resulting compaction. for simulations in which
#   output values are to reflect compaction and subsidence since the start of the simulation, enter
#   zero values for all elements of this array. (default is 0).
dcom = 0.0
# Dz is an array specifying the equivalent thickness for a system of delay interbeds. (default is
#   1).
dz = 1.0
# Nz is an array specifying the material zone numbers for systems of delay interbeds. the zone
#   number for each location in the model grid selects the hydraulic conductivity, elastic specific
#   storage, and inelastic specific storage of the interbeds. (default is 1).
nz = 1
# Format codes and unit numbers for subsidence, compaction by model layer, compaction by interbed
#   system, vertical displacement, no-delay preconsolidation, and delay preconsolidation will be
#   printed. if ids15 is none and isuboc>0 then print code 0 will be used for all data which is
#   output to the binary subsidence output file (unit=1051). the 12 entries in ids15 correspond to
#   ifm1, iun1, ifm2, iun2, ifm3, iun3, ifm4, iun4, ifm5, iun5, ifm6, and iun6 variables. (default
#   is none).
ids15 = None
# Stress period and time step range and print and save flags used to control printing and saving of
#   information generated by the sub package during program execution. each row of ids16
#   corresponds to isp1, isp2, its1, its2, ifl1, ifl2, ifl3, ifl4, ifl5, ifl6, ifl7, ifl8, ifl9,
#   ifl10, ifl11, ifl12, and ifl13 variables for isuboc entries. isp1, isp2, its1, and its2 are
#   stress period and time step ranges. ifl1 and ifl2 control subsidence printing and saving. ifl3
#   and ifl4 control compaction by model layer printing and saving. ifl5 and ifl6 control
#   compaction by interbed system printing and saving. ifl7 and ifl8 control vertical displacement
#   printing and saving. ifl9 and ifl10 control critical head for no-delay interbeds printing and
#   saving. ifl11 and ifl12 control critical head for delay interbeds printing and saving. ifl13
#   controls volumetric budget for delay interbeds printing. if ids16 is none and isuboc>0 then all
#   available subsidence output will be printed and saved to the binary subsidence output file
#   (unit=1051). (default is none).
ids16 = None

sub = flopy.modflow.mfsub.ModflowSub(model=model, ipakcb=ipakcb, isuboc=isuboc, idsave=idsave,
                                     idrest=idrest, nndb=nndb, ndb=ndb, nmz=nmz, nn=nn, ac1=ac1,
                                     ac2=ac2, itmin=itmin, ln=ln, ldn=ldn, rnb=rnb, hc=hc, sfe=sfe,
                                     sfv=sfv, com=com, dp=dp, dstart=dstart, dhc=dhc, dcom=dcom,
                                     dz=dz, nz=nz, ids15=ids15, ids16=ids16)
```

## swt


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# A flag that is used to determine if cell-by-cell budget data should be saved. if ipakcb is
#   non-zero cell-by-cell budget data will be saved. (default is 0).
ipakcb = 0
# Iswtoc is a flag used to control output of information generated by the sub package. (default is
#   0).
iswtoc = 0
nsystm = 1
# Ithk is a flag to determine how thicknesses of compressible sediments vary in response to changes
#   in saturated thickness. if ithk < 1, thickness of compressible sediments is constant. if ithk >
#   0, thickness of compressible sediments varies in response to changes in saturated thickness.
#   (default is 1).
ithk = 0
# Ivoid is a flag to determine how void ratios of compressible sediments vary in response to
#   changes in saturated thickness. if ivoid < 1, void ratio will be treated as a constant. if
#   ivoid > 0, void ratio will be treated as a variable. (default is 0).
ivoid = 0
# Istpcs is a flag to determine how initial preconsolidation stress will be obtained. if istpcs
#   does not equal 0, an array of offset values will be read in for each model layer. the offset
#   values will be added to the initial effective stress to get initial preconsolidation stress. if
#   istpcs = 0, an array with initial preconsolidation stress values will be read. (default is 1).
istpcs = 1
# Icrcc is a flag to determine how recompression and compression indices will be obtained. if icrcc
#   is not equal to 0, arrays of elastic specific storage and inelastic skeletal specific storage
#   will be read for each system of interbeds; the recompression index and compression index will
#   not be read. if icrcc = 0, arrays of recompression index and compression index will be read for
#   each system of interbeds; elastic skeletal specific storage and inelastic skeletal specific
#   storage will not be read. (default is 0).
icrcc = 0
# Lnwt is a one-dimensional array specifying the model layer assignments for each system of
#   interbeds. (default is 0).
lnwt = 0
# Izcfl is a flag to specify whether or not initial calculated values of layer-center elevation
#   will be printed. (default is 0).
izcfl = 0
# Izcfm is is a code for the format in which layer-center elevation will be printed. (default is
#   0).
izcfm = 0
# Iglfl is a flag to specify whether or not initial calculated values of geostatic stress will be
#   printed. (default is 0).
iglfl = 0
# Iglfm is a code for the format in which geostatic stress will be printed. (default is 0).
iglfm = 0
# Iestfl is a flag to specify whether or not initial calculated values of effective stress will be
#   printed. (default is 0).
iestfl = 0
# Iestfm is a code for the format in which effective stress will be printed. (default is 0).
iestfm = 0
# Ipcsfl is a flag to specify whether or not initial calculated values of preconsolidation stress
#   will be printed. (default is 0).
ipcsfl = 0
# Ipcsfm is a code for the format in which preconsolidation stress will be printed. (default is 0).
ipcsfm = 0
# Istfl is a flag to specify whether or not initial equivalent storage properties will be printed
#   for each system of interbeds. if icrcc is not equal to 0, the equivalent storage properties
#   that can be printed are recompression and compression indices (cr and cc), which are calculated
#   from elastic and inelastic skeletal specific storage (sske and sskv). if icrcc = 0, equivalent
#   storage properties that can be printed are elastic and inelastic skeletal specific storage,
#   which are calculated from the recompression and compression indices. (default is 0).
istfl = 0
# Istfm is a code for the format in which equivalent storage properties will be printed. (default
#   is 0).
istfm = 0
# Gl0 is an array specifying the geostatic stress above model layer 1. if the top of model layer 1
#   is the land surface, enter values of zero for this array. (default is 0.).
gl0 = 0.0
# Sgm is an array specifying the specific gravity of moist or unsaturated sediments. (default is
#   1.7).
sgm = 1.7000000476837158
# Sgs is an array specifying the specific gravity of saturated sediments. (default is 2.).
sgs = 2.0
# Thick is an array specifying the thickness of compressible sediments. (default is 1.).
thick = 1.0
# Sse is an array specifying the initial elastic skeletal specific storage of compressible beds.
#   sse is not used if icrcc = 0. (default is 1.).
sse = None
# Ssv is an array specifying the initial inelastic skeletal specific storage of compressible beds.
#   ssv is not used if icrcc = 0. (default is 1.).
ssv = None
# Cr is an array specifying the recompression index of compressible beds. cr is not used if icrcc
#   is not equal to 0. (default is 0.01).
cr = 0.009999999776482582
# Cc is an array specifying the compression index of compressible beds cc is not used if icrcc is
#   not equal to 0. (default is 0.25).
cc = 0.25
# Void is an array specifying the initial void ratio of compressible beds. (default is 0.82).
void = 0.8199999928474426
# Sub is an array specifying the initial compaction in each system of interbeds. compaction values
#   computed by the package are added to values in this array so that printed or stored values of
#   compaction and land subsidence may include previous components. values in this array do not
#   affect calculations of storage changes or resulting compaction. for simulations in which output
#   values will reflect compaction and subsidence since the start of the simulation, enter zero
#   values for all elements of this array. (default is 0.).
sub = 0.0
# Pcsoff is an array specifying the offset from initial effective stress to initial
#   preconsolidation stress at the bottom of the model layer in units of height of a column of
#   water. pcsoff is not used if istpcs=0. (default is 0.).
pcsoff = 0.0
# Pcs is an array specifying the initial preconsolidation stress, in units of height of a column of
#   water, at the bottom of the model layer. pcs is not used if istpcs is not equal to 0. (default
#   is 0.).
pcs = None
# Format codes and unit numbers for swtsidence, compaction by model layer, compaction by interbed
#   system, vertical displacement, preconsolidation stress, change in preconsolidation stress,
#   geostatic stress, change in geostatic stress, effective stress, void ration, thickness of
#   compressible sediments, and layer-center elecation will be printed. if ids16 is none and
#   iswtoc>0 then print code 0 will be used for all data which is output to the binary swtsidence
#   output file (unit=1054). the 26 entries in ids16 correspond to ifm1, iun1, ifm2, iun2, ifm3,
#   iun3, ifm4, iun4, ifm5, iun5, ifm6, iun6, ifm7, iun7, ifm8, iun8, ifm9, iun9, ifm10, iun11,
#   ifm12, iun12, ifm13, and iun13 variables. (default is none).
ids16 = None
# Stress period and time step range and print and save flags used to control printing and saving of
#   information generated by the sub-wt package during program execution. each row of ids17
#   corresponds to isp1, isp2, its1, its2, ifl1, ifl2, ifl3, ifl4, ifl5, ifl6, ifl7, ifl8, ifl9,
#   ifl10, ifl11, ifl12, ifl13, ifl14, ifl15, ifl16, ifl17, ifl18, ifl9, ifl20, ifl21, ifl22,
#   ifl23, ifl24, ifl25, and ifl26 variables for iswtoc entries. isp1, isp2, its1, and its2 are
#   stress period and time step ranges. ifl1 and ifl2 control subsidence printing and saving. ifl3
#   and ifl4 control compaction by model layer printing and saving. ifl5 and ifl6 control
#   compaction by interbed system printing and saving. ifl7 and ifl8 control vertical displacement
#   printing and saving. ifl9 and ifl10 control preconsolidation stress printing and saving. ifl11
#   and ifl12 control change in preconsolidation stress printing and saving. ifl13 and ifl14
#   control geostatic stress printing and saving. ifl15 and ifl16 control change in geostatic
#   stress printing and saving. ifl17 and ifl18 control effective stress printing and saving. ifl19
#   and ifl20 control change in effective stress printing and saving. ifl21 and ifl22 control void
#   ratio printing and saving. ifl23 and ifl24 control compressible bed thickness printing and
#   saving. ifl25 and ifl26 control layer-center elevation printing and saving. if ids17 is none
#   and iswtoc>0 then all available subsidence output will be printed and saved to the binary
#   subsidence output file (unit=1054). (default is none).
ids17 = None

swt = flopy.modflow.mfswt.ModflowSwt(model=model, ipakcb=ipakcb, iswtoc=iswtoc, nsystm=nsystm,
                                     ithk=ithk, ivoid=ivoid, istpcs=istpcs, icrcc=icrcc, lnwt=lnwt,
                                     izcfl=izcfl, izcfm=izcfm, iglfl=iglfl, iglfm=iglfm,
                                     iestfl=iestfl, iestfm=iestfm, ipcsfl=ipcsfl, ipcsfm=ipcsfm,
                                     istfl=istfl, istfm=istfm, gl0=gl0, sgm=sgm, sgs=sgs,
                                     thick=thick, sse=sse, ssv=ssv, cr=cr, cc=cc, void=void,
                                     sub=sub, pcsoff=pcsoff, pcs=pcs, ids16=ids16, ids17=ids17)
```

## hyd


```python
# The model object (of type :class:`flopy.modflow.mf.modflow`) to which this package will be added.
model = modflow
# The maximum number of observation points. (default is 1).
nhyd = 1
# A flag that is used to determine if hydmod data should be saved. if ihydun is non-zero hydmod
#   data will be saved. (default is 1).
ihydun = 536
# Is a user-specified value that is output if a value cannot be computed at a hydrograph location.
#   for example, the cell in which the hydrograph is located may be a no-flow cell. (default is
#   -999.)
hydnoh = -999.0
# Each row of obsdata includes data defining pckg (3 character string), arr (2 characater string),
#   intyp (1 character string) klay (int), xl (float), yl (float), hydlbl (14 character string) for
#   each observation.
obsdata = (b'BAS', b'HD', b'I', 1, 0.0, 0.0, b'HOBS1')

hyd = flopy.modflow.mfhyd.ModflowHyd(model=model, nhyd=nhyd, ihydun=ihydun, hydnoh=hydnoh,
                                     obsdata=obsdata)
```

## hob


```python
model = modflow
# Unit number where output is saved
iuhobsv = 0
# Value of the simulated equivalent written to the observation output file when the observation is
#   omitted because a cell is dry
hobdry = 0
# Time step multiplier for head observations. the product of tomulth and toffset must produce a
#   time value in units consistent with other model input. tomulth can be dimensionless or can be
#   used to convert the units of toffset to the time unit used in the simulation.
tomulth = 1.0
# List of headobservation instances containing all of the data for each observation. default is
#   none.
obs_data = None
# Name of head observation output file. if iuhobsv is greater than 0, and hobname is not provided
#   the model basename with a '.hob.out' extension will be used. default is none.
hobname = None

hob = flopy.modflow.mfhob.ModflowHob(model=model, iuhobsv=iuhobsv, hobdry=hobdry, tomulth=tomulth,
                                     obs_data=obs_data, hobname=hobname)
```

## flopy.mt3d


```python
# Name of model.  this string will be used to name the modflow input that are created with
#   write_model. (the default is 'mt3dtest')
modelname = 'swttest'
# Extension for the namefile (the default is 'nam')
namefile_ext = 'nam'
# This is a flopy modflow model object upon which this mt3dms model is based. (the default is none)
modflowmodel = modflow
ftlfilename = None
# Version of mt3dms to use (the default is 'mt3dms').
version = 'mt3dms'
# The name of the executable to use (the default is 'mt3dms.exe').
exe_name = 'mt3dms.exe'
structured = True
# Unit number for the list file (the default is 2).
listunit = None
# Model workspace.  directory name to create model data sets. (default is the present working
#   directory).
model_ws = '.'
# Location for external files (default is none).
external_path = None
# Print additional information to the screen (default is false).
verbose = False
#  (default is true).
load = True
# (default is 0)
silent = 0

mt3d = flopy.mt3d.mt.Mt3dms(modelname=modelname, namefile_ext=namefile_ext,
                            modflowmodel=modflowmodel, ftlfilename=ftlfilename, version=version,
                            exe_name=exe_name, structured=structured, listunit=listunit,
                            model_ws=model_ws, external_path=external_path, verbose=verbose,
                            load=load, silent=silent)
```

## btn


```python
# The model object (of type :class:`flopy.mt3dms.mt.mt3dms`) to which this package will be added.
model = mt3d
nlay = 1
nrow = 2
ncol = 2
nper = 1
# The total number of chemical species in the simulation. (default is none, will be changed to 1 if
#   sconc is single value)
ncomp = 1
# The total number of 'mobile' species (default is 1). mcomp must be equal or less than ncomp.
mcomp = 1
# The name of unit for time (default is 'd', for 'days'). used for identification purposes only.
tunit = 'D'
# The name of unit for length (default is 'm', for 'meters'). used for identification purposes
#   only.
lunit = 'M'
# The name of unit for mass (default is 'kg', for 'kilograms'). used for identification purposes
#   only.
munit = 'KG'
laycon = 3
delr = 1.0
delc = 1.0
htop = 1.0
dz = 1.0
# The effective porosity of the porous medium in a single porosity system, or the mobile porosity
#   in a dual-porosity medium (the immobile porosity is defined through the chemical reaction
#   package. (default is 0.25).
prsity = 0.30000001192092896
# The icbund array specifies the boundary condition type for solute species (shared by all
#   species). if icbund = 0, the cell is an inactive concentration cell; if icbund < 0, the cell is
#   a constant-concentration cell; if icbund > 0, the cell is an active concentration cell where
#   the concentration value will be calculated. (default is 1).
icbund = 1
# Ncomp) of these for multi-species simulations the starting concentration for the solute transport
#   simulation.
sconc = 0.0
# The value for indicating an inactive concentration cell. (default is 1e30).
cinact = 1e+30
# The minimum saturated thickness in a cell, expressed as the decimal fraction of its thickness,
#   below which the cell is considered inactive. (default is 0.01).
thkmin = 0.01
# A flag/format code indicating how the calculated concentration should be printed to the standard
#   output text file. format codes for printing are listed in table 3 of the mt3dms manual. if
#   ifmtcn > 0 printing is in wrap form; ifmtcn < 0 printing is in strip form; if ifmtcn = 0
#   concentrations are not printed. (default is 0).
ifmtcn = 0
# A flag/format code indicating how the number of particles should be printed to the standard
#   output text file. the convention is the same as for ifmtcn. (default is 0).
ifmtnp = 0
# A flag/format code indicating how the calculated retardation factor should be printed to the
#   standard output text file. the convention is the same as for ifmtcn. (default is 0).
ifmtrf = 0
# A flag/format code indicating how the distance-weighted dispersion coefficient should be printed
#   to the standard output text file. the convention is the same as for ifmtcn. (default is 0).
ifmtdp = 0
# A logical flag indicating whether the concentration solution should be saved in an unformatted
#   file. (default is true).
savucn = True
# A flag indicating (i) the frequency of the output and (ii) whether the output frequency is
#   specified in terms of total elapsed simulation time or the transport step number. if nprs > 0
#   results will be saved at the times as specified in timprs; if nprs = 0, results will not be
#   saved except at the end of simulation; if nprs < 0, simulation results will be saved whenever
#   the number of transport steps is an even multiple of nprs. (default is 0).
nprs = 0
# The total elapsed time at which the simulation results are saved. the number of entries in timprs
#   must equal nprs. (default is none).
timprs = None
obs = None
nprobs = 1
chkmas = True
nprmas = 1
perlen = 1.0
nstp = 1
tsmult = 1.0
ssflag = None
dt0 = 0.0
mxstrn = 50000
ttsmult = 1.0
ttsmax = 0.0
species_names = []

btn = flopy.mt3d.mtbtn.Mt3dBtn(model=model, nlay=nlay, nrow=nrow, ncol=ncol, nper=nper,
                               ncomp=ncomp, mcomp=mcomp, tunit=tunit, lunit=lunit, munit=munit,
                               laycon=laycon, delr=delr, delc=delc, htop=htop, dz=dz,
                               prsity=prsity, icbund=icbund, sconc=sconc, cinact=cinact,
                               thkmin=thkmin, ifmtcn=ifmtcn, ifmtnp=ifmtnp, ifmtrf=ifmtrf,
                               ifmtdp=ifmtdp, savucn=savucn, nprs=nprs, timprs=timprs, obs=obs,
                               nprobs=nprobs, chkmas=chkmas, nprmas=nprmas, perlen=perlen,
                               nstp=nstp, tsmult=tsmult, ssflag=ssflag, dt0=dt0, mxstrn=mxstrn,
                               ttsmult=ttsmult, ttsmax=ttsmax, species_names=species_names)
```

## adv


```python
# The model object (of type :class:`flopy.mt3d.mt.mt3dms`) to which this package will be added.
model = mt3d
# Mixelm is an integer flag for the advection solution option. mixelm = 0, the standard
#   finite-difference method with upstream or central-in-space weighting, depending on the value of
#   nadvfd; = 1, the forward-tracking method of characteristics (moc); = 2, the backward-tracking
#   modified method of characteristics (mmoc); = 3, the hybrid method of characteristics (hmoc)
#   with moc or mmoc automatically and dynamically selected; = -1, the third-order tvd scheme
#   (ultimate).
mixelm = 3
# Percel is the courant number (i.e., the number of cells, or a fraction of a cell) advection will
#   be allowed in any direction in one transport step. for implicit finite-difference or
#   particle-tracking-based schemes, there is no limit on percel, but for accuracy reasons, it is
#   generally not set much greater than one. note, however, that the percel limit is checked over
#   the entire model grid. thus, even if percel > 1, advection may not be more than one cell's
#   length at most model locations. for the explicit finite-difference or the third-order tvd
#   scheme, percel is also a stability constraint which must not exceed one and will be
#   automatically reset to one if a value greater than one is specified.
percel = 0.75
# Mxpart is the maximum total number of moving particles allowed and is used only when mixelm = 1
#   or 3.
mxpart = 800000
# Nadvfd is an integer flag indicating which weighting scheme should be used; it is needed only
#   when the advection term is solved using the implicit finite- difference method. nadvfd = 0 or
#   1, upstream weighting (default); = 2,central-in-space weighting.
nadvfd = 1
# Itrack is a flag indicating which particle-tracking algorithm is selected for the
#   eulerian-lagrangian methods. itrack = 1, the first-order euler algorithm is used. = 2, the
#   fourth-order runge-kutta algorithm is used; this option is computationally demanding and may be
#   needed only when percel is set greater than one. = 3, the hybrid first- and fourth-order
#   algorithm is used; the runge-kutta algorithm is used in sink/source cells and the cells next to
#   sinks/sources while the euler algorithm is used elsewhere.
itrack = 3
# Is a concentration weighting factor between 0.5 and 1. it is used for operator splitting in the
#   particle- tracking-based methods. the value of 0.5 is generally adequate. the value of wd may
#   be adjusted to achieve better mass balance. generally, it can be increased toward 1.0 as
#   advection becomes more dominant.
wd = 0.5
# Is a small relative cell concentration gradient below which advective transport is considered
dceps = 1e-05
# Nplane is a flag indicating whether the random or fixed pattern is selected for initial placement
#   of moving particles. if nplane = 0, the random pattern is selected for initial placement.
#   particles are distributed randomly in both the horizontal and vertical directions by calling a
#   random number generator (figure 18b). this option is usually preferred and leads to smaller
#   mass balance discrepancy in nonuniform or diverging/converging flow fields. if nplane > 0, the
#   fixed pattern is selected for initial placement. the value of nplane serves as the number of
#   vertical 'planes' on which initial particles are placed within each cell block (figure 18a).
#   the fixed pattern may work better than the random pattern only in relatively uniform flow
#   fields. for two-dimensional simulations in plan view, set nplane = 1. for cross sectional or
#   three-dimensional simulations, nplane = 2 is normally adequate. increase nplane if more
#   resolution in the vertical direction is desired.
nplane = 2
# Npl is the number of initial particles per cell to be placed at cells where the relative cell
#   concentration gradient is less than or equal to dceps. generally, npl can be set to zero since
#   advection is considered insignificant when the relative cell concentration gradient is less
#   than or equal to dceps. setting npl equal to nph causes a uniform number of particles to be
#   placed in every cell over the entire grid (i.e., the uniform approach).
npl = 10
# Nph is the number of initial particles per cell to be placed at cells where the relative cell
#   concentration gradient is greater than dceps. the selection of nph depends on the nature of the
#   flow field and also the computer memory limitation. generally, a smaller number should be used
#   in relatively uniform flow fields and a larger number should be used in relatively nonuniform
#   flow fields. however, values exceeding 16 in two-dimensional simulation or 32 in three-
#   dimensional simulation are rarely necessary. if the random pattern is chosen, nph particles are
#   randomly distributed within the cell block. if the fixed pattern is chosen, nph is divided by
#   nplane to yield the number of particles to be placed per vertical plane, which is rounded to
#   one of the values shown in figure 30.
nph = 40
# Is the minimum number of particles allowed per cell. if the number of particles in a cell at the
#   end of a transport step is fewer than npmin, new particles are inserted into that cell to
#   maintain a sufficient number of particles. npmin can be set to zero in relatively uniform flow
#   fields and to a number greater than zero in diverging/converging flow fields. generally, a
#   value between zero and four is adequate.
npmin = 5
# Npmax is the maximum number of particles allowed per cell. if the number of particles in a cell
#   exceeds npmax, all particles are removed from that cell and replaced by a new set of particles
#   equal to nph to maintain mass balance. generally, npmax can be set to approximately two times
#   of nph.
npmax = 80
# S a flag indicating whether the random or fixed pattern is selected for initial placement of
#   particles to approximate sink cells in the mmoc scheme. the convention is the same as that for
#   nplane. it is generally adequate to set nlsink equivalent to nplane.
nlsink = 0
# Is the number of particles used to approximate sink cells in the mmoc scheme. the convention is
#   the same as that for nph. it is generally adequate to set npsink equivalent to nph.
npsink = 15
# Dchmoc is the critical relative concentration gradient for controlling the selective use of
#   either moc or mmoc in the hmoc solution scheme. the moc solution is selected at cells where the
#   relative concentration gradient is greater than dchmoc. the mmoc solution is selected at cells
#   where the relative concentration gradient is less than or equal to dchmoc.
dchmoc = 0.0001

adv = flopy.mt3d.mtadv.Mt3dAdv(model=model, mixelm=mixelm, percel=percel, mxpart=mxpart,
                               nadvfd=nadvfd, itrack=itrack, wd=wd, dceps=dceps, nplane=nplane,
                               npl=npl, nph=nph, npmin=npmin, npmax=npmax, nlsink=nlsink,
                               npsink=npsink, dchmoc=dchmoc)
```

## dsp


```python
# The model object (of type :class:`flopy.mt3d.mt.mt3dms`) to which this package will be added.
model = mt3d
# Al is the longitudinal dispersivity, for every cell of the model grid (unit, l). (default is
#   0.01)
al = 0.009999999776482582
# S a 1d real array defining the ratio of the horizontal transverse dispersivity to the
#   longitudinal dispersivity. each value in the array corresponds to one model layer. some recent
#   field studies suggest that trpt is generally not greater than 0.1. (default is 0.1)
trpt = 0.10000000149011612
# Is the ratio of the vertical transverse dispersivity to the longitudinal dispersivity. each value
#   in the array corresponds to one model layer. some recent field studies suggest that trpt is
#   generally not greater than 0.01.  set trpv equal to trpt to use the standard isotropic
#   dispersion model (equation 10 in chapter 2). otherwise, the modified isotropic dispersion model
#   is used (equation 11 in chapter 2). (default is 0.01)
trpv = 0.009999999776482582
# Multidiff option is used. dmcoef is the effective molecular diffusion coefficient (unit, l2t-1).
#   set dmcoef = 0 if the effect of molecular diffusion is considered unimportant. each value in
#   the array corresponds to one model layer. the value for dmcoef applies only to species 1.  see
#   kwargs for entering dmcoef for other species. (default is 1.e-9).
dmcoef = 9.999999717180685e-10
# To activate the component-dependent diffusion option, a keyword input record must be inserted to
#   the beginning of the dispersion (dsp) input file. the symbol $ in the first column of an input
#   line signifies a keyword input record containing one or more predefined keywords. above the
#   keyword input record, comment lines marked by the symbol # in the first column are allowed.
#   comment lines are processed but have no effect on the simulation. furthermore, blank lines are
#   also acceptable above the keyword input record. below the keyword input record, the format of
#   the dsp input file must remain unchanged from the previous versions except for the diffusion
#   coefficient as explained below. if no keyword input record is specified, the input file remains
#   backward compatible with all previous versions of mt3dms. the predefined keyword for the
#   component-dependent diffusion option is multidiffusion. the keyword is case insensitive so
#   ''multidiffusion'' is equivalent to either ''multidiffusion'' or ''multidiffusion''. if this
#   keyword is specified in the keyword input record that has been inserted into the beginning of
#   the dsp input file, the component-dependent diffusion option has been activated and the user
#   needs to specify one diffusion coefficient for each mobile solute component and at each model
#   cell. this is done by specifying one mobile component at a time, from the first component to
#   the last component (mcomp). for each mobile component, the real array reader utility (rarray)
#   is used to input the 3-d diffusion coefficient array, one model layer at a time. (default is
#   false)
multiDiff = False

dsp = flopy.mt3d.mtdsp.Mt3dDsp(model=model, al=al, trpt=trpt, trpv=trpv, dmcoef=dmcoef,
                               multiDiff=multiDiff)
```

## ssm


```python
# The model object (of type :class:`flopy.mt3d.mt.mt3dms`) to which this package will be added.
model = mt3d
# Crch is the concentration of recharge for species 1. if the recharge flux is positive, it acts as
#   a source whose concentration can be specified as desired. if the recharge flux is negative, it
#   acts as a sink (discharge) whose concentration is always set equal to the concentration of
#   groundwater at the cell where discharge occurs. note that the location and flow rate of
#   recharge/discharge are obtained from the flow model directly through the unformatted
#   flow-transport link file.  crch can be specified as an array, if the array is constant for the
#   entire simulation.  if crch changes by stress period, then the user must provide a dictionary,
#   where the key is the stress period number (zero based) and the value is the recharge array.
#   the recharge concentration can be specified for additional species by passing additional
#   arguments to the mt3dssm constructor.  for example, to specify the recharge concentration for
#   species two one could use crch2={0: 0., 1: 10*np.ones((nlay, nrow, ncol), dtype=np.float)} as
#   and additional keyword argument that is passed to mt3dssm when making the ssm object.
crch = None
# Is the concentration of evapotranspiration flux for species 1. evapotranspiration is the only
#   type of sink whose concentration may be specified externally. note that the concentration of a
#   sink cannot be greater than that of the aquifer at the sink cell. thus, if the sink
#   concentration is specified greater than that of the aquifer, it is automatically set equal to
#   the concentration of the aquifer. also note that the location and flow rate of
#   evapotranspiration are obtained from the flow model directly through the unformatted
#   flow-transport link file.  for multi-species simulations, see crch for a description of how to
#   specify additional concentrations arrays for each species.
cevt = None
mxss = 8
# Keys in the dictionary are stress zero-based stress period numbers; values in the dictionary are
#   recarrays of ssm boundaries.  the dtype for the recarray can be obtained using ssm.dtype (after
#   the ssm package has been created).  the default dtype for the recarray is np.dtype([('k',
#   np.int), ("i", np.int), ("j", np.int), ("css", np.float32), ("itype", np.int), ((cssms(n),
#   np.float), n=1, ncomp)]) if there are more than one component species, then additional entries
#   will be added to the dtype as indicated by cssm(n). note that if the number of dictionary
#   entries is less than the number of stress periods, then the last recarray of boundaries will
#   apply until the end of the simulation. full details of all options to specify
#   stress_period_data can be found in the flopy3_multi-component_ssm ipython notebook in the
#   notebook subdirectory of the examples directory. css is the specified source concentration or
#   mass-loading rate, depending on the value of itype, in a single-species simulation, (for a
#   multispecies simulation, css is not used, but a dummy value still needs to be entered here.)
#   note that for most types of sources, css is interpreted as the source concentration with the
#   unit of mass per unit volume (ml-3), which, when multiplied by its corresponding flow rate
#   (l3t-1) from the flow model, yields the mass-loading rate (mt-1) of the source. for a special
#   type of sources (itype = 15), css is taken directly as the mass-loading rate (mt-1) of the
#   source so that no flow rate is required from the flow model. furthermore, if the source is
#   specified as a constant-concentration cell (itype = -1), the specified value of css is assigned
#   directly as the concentration of the designated cell. if the designated cell is also associated
#   with a sink/source term in the flow model, the flow rate is not used. itype is an integer
#   indicating the type of the point source.  an itype dictionary can be retrieved from the ssm
#   object as itype = mt3d.mt3dssm.itype_dict() (cssms(n), n=1, ncomp) defines the concentrations
#   of a point source for multispecies simulation with ncomp>1. in a multispecies simulation, it is
#   necessary to define the concentrations of all species associated with a point source. as an
#   example, if a chemical of a certain species is injected into a multispecies system, the
#   concentration of that species is assigned a value greater than zero while the concentrations of
#   all other species are assigned zero. cssms(n) can be entered in free format, separated by a
#   comma or space between values. several important notes on assigning concentration for the
#   constant-concentration condition (itype = -1) are listed below: the constant-concentration
#   condition defined in this input file takes precedence to that defined in the basic transport
#   package input file. in a multiple stress period simulation, a constant-concentration cell, once
#   defined, will remain a constant- concentration cell in the duration of the simulation, but its
#   concentration value can be specified to vary in different stress periods. in a multispecies
#   simulation, if it is only necessary to define different constant-concentration conditions for
#   selected species at the same cell location, specify the desired concentrations for those
#   species, and assign a negative value for all other species. the negative value is a flag used
#   by mt3dms to skip assigning the constant-concentration condition for the designated species.
stress_period_data = None
# Dtype to use for the recarray of boundaries.  if left as none (the default) then the dtype will
#   be automatically constructed.
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('css', '<f4'), ('itype', '<i8')])

ssm = flopy.mt3d.mtssm.Mt3dSsm(model=model, crch=crch, cevt=cevt, mxss=mxss,
                               stress_period_data=stress_period_data, dtype=dtype)
```

## rct


```python
# The model object (of type :class:`flopy.mt3dms.mt.mt3dms`) to which this package will be added.
model = mt3d
# Isothm is a flag indicating which type of sorption (or dual-domain mass transfer) is simulated:
#   isothm = 0, no sorption is simulated; isothm = 1, linear isotherm (equilibrium-controlled);
#   isothm = 2, freundlich isotherm (equilibrium-controlled); isothm = 3, langmuir isotherm
#   (equilibrium-controlled); isothm = 4, first-order kinetic sorption (nonequilibrium); isothm =
#   5, dual-domain mass transfer (without sorption); isothm = 6, dual-domain mass transfer (with
#   sorption). (default is 0).
isothm = 0
# Ireact is a flag indicating which type of kinetic rate reaction is simulated: ireact = 0, no
#   kinetic rate reaction is simulated; ireact = 1, first-order irreversible reaction. note that
#   this reaction package is not intended for modeling chemical reactions between species. an
#   add-on reaction package developed specifically for that purpose may be used. (default is 0).
ireact = 0
# Igetsc is an integer flag indicating whether the initial concentration for the nonequilibrium
#   sorbed or immobile phase of all species should be read when nonequilibrium sorption (isothm =
#   4) or dual-domain mass transfer (isothm = 5 or 6) is simulated: igetsc = 0, the initial
#   concentration for the sorbed or immobile phase is not read. by default, the sorbed phase is
#   assumed to be in equilibrium with the dissolved phase (isothm = 4), and the immobile domain is
#   assumed to have zero concentration (isothm = 5 or 6). igetsc > 0, the initial concentration for
#   the sorbed phase or immobile liquid phase of all species will be read. (default is 1).
igetsc = 1
# Rhob is the bulk density of the aquifer medium (unit, ml-3). rhob is used if isothm = 1, 2, 3, 4,
#   or 6. if rhob is not user-specified and isothem is not 5 then rhob is set to 1.8e3. (default is
#   none)
rhob = 1800.0
# Prsity2 is the porosity of the immobile domain (the ratio of pore spaces filled with immobile
#   fluids over the bulk volume of the aquifer medium) when the simulation is intended to represent
#   a dual-domain system. prsity2 is used if isothm = 5 or 6. if prsity2 is not user- specified and
#   isothm = 5 or 6 then prsity2 is set to 0.1. (default is none)
prsity2 = 0.10000000149011612
# Srconc is the user-specified initial concentration for the sorbed phase of the first species if
#   isothm = 4 (unit, mm-1). note that for equilibrium-controlled sorption, the initial
#   concentration for the sorbed phase cannot be specified. srconc is the user-specified initial
#   concentration of the first species for the immobile liquid phase if isothm = 5 or 6 (unit,
#   ml-3). if srconc is not user-specified and isothm = 4, 5, or 6 then srconc is set to 0.
#   (default is none).
srconc = 0.0
# Sp1 is the first sorption parameter for the first species. the use of sp1 depends on the type of
#   sorption selected (the value of isothm). for linear sorption (isothm = 1) and nonequilibrium
#   sorption (isothm = 4), sp1 is the distribution coefficient (kd) (unit, l3m-1). for freundlich
#   sorption (isothm = 2), sp1 is the freundlich equilibrium constant (kf) (the unit depends on the
#   freundlich exponent a). for langmuir sorption (isothm = 3), sp1 is the langmuir equilibrium
#   constant (kl) (unit, l3m-1 ). for dual-domain mass transfer without sorption (isothm = 5), sp1
#   is not used, but still must be entered. for dual-domain mass transfer with sorption (isothm =
#   6), sp1 is also the distribution coefficient (kd) (unit, l3m-1). if sp1 is not specified and
#   isothm > 0 then sp1 is set to 0. (default is none).
sp1 = 0.0
# Sp2 is the second sorption or dual-domain model parameter for the first species. the use of sp2
#   depends on the type of sorption or dual-domain model selected. for linear sorption (isothm =
#   1), sp2 is read but not used. for freundlich sorption (isothm = 2), sp2 is the freundlich
#   exponent a. for langmuir sorption (isothm = 3), sp2 is the total concentration of the sorption
#   sites available ( s ) (unit, mm-1). for nonequilibrium sorption (isothm = 4), sp2 is the
#   first-order mass transfer rate between the dissolved and sorbed phases (unit, t-1). for
#   dual-domain mass transfer (isothm = 5 or 6), sp2 is the first-order mass transfer rate between
#   the two domains (unit, t-1). if sp2 is not specified and isothm > 0 then sp2 is set to 0.
#   (default is none).
sp2 = 0.0
# Rc1 is the first-order reaction rate for the dissolved (liquid) phase for the first species
#   (unit, t-1). rc1 is not used ireact = 0. if a dual-domain system is simulated, the reaction
#   rates for the liquid phase in the mobile and immobile domains are assumed to be equal. if rc1
#   is not specified and ireact > 0 then rc1 is set to 0. (default is none).
rc1 = 0.0
# Rc2 is the first-order reaction rate for the sorbed phase for the first species (unit, t-1). rc2
#   is not used ireact = 0. if a dual-domain system is simulated, the reaction rates for the sorbed
#   phase in the mobile and immobile domains are assumed to be equal. generally, if the reaction is
#   radioactive decay, rc2 should be set equal to rc1, while for biodegradation, rc2 may be
#   different from rc1. note that rc2 is read but not used, if no sorption is included in the
#   simulation. if rc2 is not specified and ireact > 0 then rc2 is set to 0. (default is none).
rc2 = 0.0

rct = flopy.mt3d.mtrct.Mt3dRct(model=model, isothm=isothm, ireact=ireact, igetsc=igetsc, rhob=rhob,
                               prsity2=prsity2, srconc=srconc, sp1=sp1, sp2=sp2, rc1=rc1, rc2=rc2)
```

## gcg


```python
# The model object (of type :class:`flopy.mt3d.mt.mt3dms`) to which this package will be added.
model = mt3d
# Is the maximum number of outer iterations; it should be set to an integer greater than one only
#   when a nonlinear sorption isotherm is included in simulation. (default is 1)
mxiter = 1
# Is the maximum number of inner iterations; a value of 30-50 should be adequate for most problems.
#   (default is 50)
iter1 = 50
# Is the type of preconditioners to be used with the lanczos/orthomin acceleration scheme: = 1,
#   jacobi = 2, ssor = 3, modified incomplete cholesky (mic) (mic usually converges faster, but it
#   needs significantly more memory) (default is 3)
isolve = 3
# Is an integer flag for treatment of dispersion tensor cross terms: = 0, lump all dispersion cross
#   terms to the right-hand-side (approximate but highly efficient). = 1, include full dispersion
#   tensor (memory intensive). (default is 0)
ncrs = 0
# Is the relaxation factor for the ssor option; a value of 1.0 is generally adequate. (default is
#   1)
accl = 1
# Is the convergence criterion in terms of relative concentration; a real value between 10-4 and
#   10-6 is generally adequate. (default is 1.e-5)
cclose = 1e-05
# Iprgcg is the interval for printing the maximum concentration changes of each iteration. set
#   iprgcg to zero as default for printing at the end of each stress period. (default is 0)
iprgcg = 0

gcg = flopy.mt3d.mtgcg.Mt3dGcg(model=model, mxiter=mxiter, iter1=iter1, isolve=isolve, ncrs=ncrs,
                               accl=accl, cclose=cclose, iprgcg=iprgcg)
```

## tob


```python
model = mt3d
outnam = 'tob_output'
CScale = 1.0
FluxGroups = []
FScale = 1.0
iOutFlux = 0

tob = flopy.mt3d.mttob.Mt3dTob(model=model, outnam=outnam, CScale=CScale, FluxGroups=FluxGroups,
                               FScale=FScale, iOutFlux=iOutFlux)
```

## lkt


```python
# The model object (of type :class:`flopy.mt3dms.mt.mt3dms`) to which this package will be added.
model = mt3d
# Is equal to the number of simulated lakes as specified in the flow simulation
nlkinit = 0
# Must be greater than or equal to the sum total of boundary conditions  applied to each lake
mxlkbc = 0
# Is equal to the unit number on which lake-by-lake transport information will be printed.  this
#   unit number must appear in the nam input file  required for every mt3d-usgs simulation.
icbclk = None
# Specifies whether or not evaporation as simulated in the flow solution  will act as a mass sink.
#   = 0, mass does not exit the model via simulated lake evaporation != 0, mass may leave the lake
#   via simulated lake evaporation
ietlak = 0
# Is a vector of real numbers representing the initial concentrations in  the simulated lakes.  the
#   length of the vector is equal to the number  of simulated lakes, nlkinit.  initial lake
#   concentrations should be  in the same order as the lakes appearing in the lak input file
#   corresponding to the modflow simulation.
coldlak = 0.0
lk_stress_period_data = None
dtype = None

lkt = flopy.mt3d.mtlkt.Mt3dLkt(model=model, nlkinit=nlkinit, mxlkbc=mxlkbc, icbclk=icbclk,
                               ietlak=ietlak, coldlak=coldlak,
                               lk_stress_period_data=lk_stress_period_data, dtype=dtype)
```

## sft


```python
# The model object (of type :class:`flopy.mt3dms.mt.mt3dms`) to which this package will be added.
model = mt3d
# Is the number of simulated stream reaches (in sfr2, the number of stream reaches is greater than
#   or equal to the number of stream segments).  this is equal to nstrm found on the first line of
#   the sfr2 input file.  if nsfinit > 0 then surface-water transport is solved in the stream
#   network while taking into account groundwater exchange and precipitation and evaporation
#   sources and sinks. otherwise, if nsfinit < 0, the surface-water network as represented by the
#   sfr2 flow package merely acts as a boundary condition to the groundwater transport problem;
#   transport in the surface-water network is not simulated.
nsfinit = 0
# Is the maximum number of stream boundary conditions.
mxsfbc = 0
# Is an integer value that directs mt3d-usgs to write reach-by-reach concentration information to
#   unit icbcsf.
icbcsf = 0
# Is the unit number of the output file for simulated concentrations at specified gage locations.
#   the nam file must also list the unit number to which observation information will be written.
ioutobs = None
# Specifies whether or not mass will exit the surface-water network with simulated evaporation.  if
#   ietsfr = 0, then mass does not leave via stream evaporation.  if ietsfr > 0, then mass is
#   allowed to exit the simulation with the simulated evaporation.
ietsfr = 0
# Specifies the numerical technique that will be used to solve the transport problem in the surface
#   water network.  the first release of mt3d-usgs (version 1.0) only allows for a
#   finite-difference formulation and regardless of what value the user specifies, the variable
#   defaults to 1, meaning the finite-difference solution is invoked.
isfsolv = 1
# Is the stream solver time weighting factor.  ranges between 0.0 and 1.0.  values of 0.0, 0.5, or
#   1.0 correspond to explicit, crank-nicolson, and fully implicit schemes, respectively.
wimp = 0.5
# Is the space weighting factor employed in the stream network solver. ranges between 0.0 and 1.0.
#   values of 0.0 and 1.0 correspond to a central-in-space and upstream weighting factors,
#   respectively.
wups = 1.0
# Is the closure criterion for the sft solver
cclosesf = 1e-06
# Limits the maximum number of iterations the sft solver can use to find a solution of the stream
#   transport problem.
mxitersf = 10
# Is the courant constraint specific to the sft time step, its value has no bearing upon the
#   groundwater transport solution time step.
crntsf = 1.0
# A flag to print sft solution information to the standard output file. iprtxmd = 0 means no sft
#   solution information is printed; iprtxmd = 1 means sft solution summary information is printed
#   at the end of every mt3d-usgs outer iteration; and iprtxmd = 2 means sft solution details are
#   written for each sft outer iteration that calls the xmd solver that solved sft equations.
iprtxmd = 0
# Represents the initial concentrations in the surface water network. the length of the array is
#   equal to the number of stream reaches and starting concentration values should be entered in
#   the same order that individual reaches are entered for record set 2 in the sfr2 input file.
coldsf = 0.0
# Is the dispersion coefficient [l2 t-1] for each stream reach in the simulation and can vary for
#   each simulated component of the simulation.  that is, the length of the array is equal to the
#   number of simulated stream reaches times the number of simulated components. values of
#   dispersion for each reach should be entered in the same order that individual reaches are
#   entered for record set 2 in the sfr2 input file.  the first nstrm entries correspond to ncomp =
#   1, with subsequent entries for each ncomp simulated species.
dispsf = 0.0
# Specifies the number of surface flow observation points for monitoring simulated concentrations
#   in streams.
nobssf = 0
obs_sf = None
sf_stress_period_data = None
dtype = None

sft = flopy.mt3d.mtsft.Mt3dSft(model=model, nsfinit=nsfinit, mxsfbc=mxsfbc, icbcsf=icbcsf,
                               ioutobs=ioutobs, ietsfr=ietsfr, isfsolv=isfsolv, wimp=wimp,
                               wups=wups, cclosesf=cclosesf, mxitersf=mxitersf, crntsf=crntsf,
                               iprtxmd=iprtxmd, coldsf=coldsf, dispsf=dispsf, nobssf=nobssf,
                               obs_sf=obs_sf, sf_stress_period_data=sf_stress_period_data,
                               dtype=dtype)
```

## uzt


```python
# The model object (of type :class:`flopy.mt3dms.mt.mt3dms`) to which this package will be added.
model = mt3d
# Is the maximum number of uzf1 connections and is equal to the number  of non-zero entries in the
#   irnbnd array found in the uzf1 input file  for modflow.  keep in mind there is potential for
#   every cell with a  non-zero irnbnd entry to pass water to either a lake or stream segment
mxuzcon = 0
# Is the unit number to which unsaturated-zone concentration will be  written out.
icbcuz = None
# Is a flag that indicates whether or not et is being simulated in the  uzf1 flow package.  if et
#   is not being simulated, iet informs fmi  package not to look for uzet and gwet arrays in the
#   flow-tranpsort  link file.
iet = 0
# Specifies which row/column indices variably-saturated transport will  be simulated in.    >0
#   indicates variably-saturated transport will be simulated;    =0  indicates variably-saturated
#   transport will not be simulated;    <0  corresponds to iuzfbnd < 0 in the uzf1 input package,
#   meaning         that user-supplied values for finf are specified recharge and        therefore
#   transport through the unsaturated zone is not         simulated.
iuzfbnd = None
# Starting water content.  for cells above the water tables, this value  can range between residual
#   and saturated water contents.  in cells  below the water table, this value will be eqal to
#   saturated water  content (i.e., effective porosity).  for cells containing the water  table, a
#   volume average approach needs to be used to calculate an  equivalent starting water content.
wc = 0.0
# Starting saturated thickness for each cell in the simulation.  for  cells residing above the
#   starting water table, sdh=0. in completely  saturated cells, sdh is equal to total thickness.
#   for cells  containing the water table, sdh equals the water table elevation minus  the cell
#   bottom elevation.
sdh = 0.0
# Is the concentration of the infiltrating flux for a particular species. an array for each species
#   will be read.
cuzinf = None
# Is the concentration of et fluxes originating from the unsaturated  zone.  as a default, this
#   array is set equal to 0 and only overridden  if the user specifies incuzet > 1.  if empirical
#   evidence suggest  volatilization of simulated constituents from the unsaturated zone,  this may
#   be one mechanism for simulating this process, though it would  depend on the amount of
#   simulated et originating from the unsaturated  zone.  an array for each species will be read.
cuzet = None
# Is the concentration of et fluxes originating from the saturated zone.  as a default, this array
#   is set equal to 0 and only overridden if the  user specifies incuzet > 1.  an array for each
#   species will be read.
cgwet = None

uzt = flopy.mt3d.mtuzt.Mt3dUzt(model=model, mxuzcon=mxuzcon, icbcuz=icbcuz, iet=iet,
                               iuzfbnd=iuzfbnd, wc=wc, sdh=sdh, cuzinf=cuzinf, cuzet=cuzet,
                               cgwet=cgwet)
```

## flopy.seawat


```python
# Name of model.  this string will be used to name the seawat input that are created with
#   write_model. (the default is 'swttest')
modelname = 'swttest'
# Extension for the namefile (the default is 'nam')
namefile_ext = 'nam'
modflowmodel = modflow
mt3dmodel = mt3d
# Version of seawat to use (the default is 'seawat').
version = 'seawat'
# The name of the executable to use (the default is 'swt_v4.exe').
exe_name = 'swt_v4'
structured = True
# Unit number for the list file (the default is 2).
listunit = 2
# Model workspace.  directory name to create model data sets. (default is the present working
#   directory).
model_ws = '.'
# Location for external files (default is none).
external_path = None
# Print additional information to the screen (default is false).
verbose = False
#  (default is true).
load = True
# (default is 0)
silent = 0

seawat = flopy.seawat.swt.Seawat(modelname=modelname, namefile_ext=namefile_ext,
                                 modflowmodel=modflowmodel, mt3dmodel=mt3dmodel, version=version,
                                 exe_name=exe_name, structured=structured, listunit=listunit,
                                 model_ws=model_ws, external_path=external_path, verbose=verbose,
                                 load=load, silent=silent)
```

## vdf


```python
# The model object (of type :class:`flopy.seawat.swt.seawat`) to which this package will be added.
model = seawat
mtdnconc = 1
# Is a flag that determines the method for calculating the internodal density values used to
#   conserve fluid mass. if mfnadvfd = 2, internodal conductance values used to conserve fluid mass
#   are calculated using a central-in-space algorithm. if mfnadvfd <> 2, internodal conductance
#   values used to conserve fluid mass are calculated using an upstream-weighted algorithm.
mfnadvfd = 1
# Is a flag used to determine the flow and transport coupling procedure. if nswtcpl = 0 or 1, flow
#   and transport will be explicitly coupled using a one-timestep lag. the explicit coupling option
#   is normally much faster than the iterative option and is recommended for most applications. if
#   nswtcpl > 1, nswtcpl is the maximum number of non-linear coupling iterations for the flow and
#   transport solutions. seawat-2000 will stop execution after nswtcpl iterations if convergence
#   between flow and transport has not occurred. if nswtcpl = -1, the flow solution will be
#   recalculated only for: the first transport step of the simulation, or the last transport step
#   of the modflow timestep, or the maximum density change at a cell is greater than dnscrit.
nswtcpl = 1
# Is a flag used to activate the variable-density water-table corrections (guo and langevin, 2002,
#   eq. 82). if iwtable = 0, the water-table correction will not be applied. if iwtable > 0, the
#   water-table correction will be applied.
iwtable = 1
# Is the minimum fluid density. if the resulting density value calculated with the equation of
#   state is less than densemin, the density value is set to densemin. if densemin = 0, the
#   computed fluid density is not limited by densemin (this is the option to use for most
#   simulations). if densemin > 0, a computed fluid density less than densemin is automatically
#   reset to densemin.
densemin = 1.0
# Is the maximum fluid density. if the resulting density value calculated with the equation of
#   state is greater than densemax, the density value is set to densemax. if densemax = 0, the
#   computed fluid density is not limited by densemax (this is the option to use for most
#   simulations). if densemax > 0, a computed fluid density larger than densemax is automatically
#   reset to densemax.
densemax = 1.025
# Is a user-specified density value. if nswtcpl is greater than 1, dnscrit is the convergence
#   crite- rion, in units of fluid density, for convergence between flow and transport. if the
#   maximum fluid density difference between two consecutive implicit coupling iterations is not
#   less than dnscrit, the program will continue to iterate on the flow and transport equations, or
#   will terminate if nswtcpl is reached. if nswtcpl is -1, dnscrit is the maximum density
#   threshold, in units of fluid density. if the fluid density change (between the present
#   transport timestep and the last flow solution) at one or more cells is greater than dnscrit,
#   then seawat_v4 will update the flow field (by solving the flow equation with the updated
#   density field).
dnscrit = 0.01
# Is the fluid density at the reference concentration, temperature, and pressure. for most
#   simulations, denseref is specified as the density of freshwater at 25 degrees c and at a
#   reference pressure of zero.
denseref = 1.0
denseslp = 0.025
# Is the reference concentration (c0) for species, mtrhospec. for most simulations, crhoref should
#   be specified as zero. if mt3drhoflg > 0, crhoref is assumed to equal zero (as was done in
#   previous versions of seawat).
crhoref = 0
# Is the length of the first transport timestep used to start the simulation if both of the
#   following two condi- tions are met: 1. the imt process is active, and 2. transport timesteps
#   are calculated as a function of the user-specified courant number (the mt3dms input variable,
#   percel, is greater than zero).
firstdt = 0.001
# Is a flag. indense is read only if mt3drhoflg is equal to zero. if indense < 0, values for the
#   dense array will be reused from the previous stress period. if it is the first stress period,
#   values for the dense array will be set to denseref. if indense = 0, values for the dense array
#   will be set to denseref. if indense >= 1, values for the dense array will be read from item 7.
#   if indense = 2, values read for the dense array are assumed to represent solute concentration,
#   and will be converted to density values using the equation of state.
indense = 1
# A float or array of floats (nlay, nrow, ncol) should be assigned as values to a dictionary
#   related to keys of period number.  dense is the fluid density array read for each layer using
#   the modflow-2000 u2drel array reader. the dense array is read only if mt3drhoflg is equal to
#   zero. the dense array may also be entered in terms of solute concentration, or any other units,
#   if indense is set to 2 and the constants used in the density equation of state are specified
#   appropriately.
dense = None
# Is the number of mt3dms species to be used in the equation of state for fluid density. this value
#   is read only if mt3drhoflg = -1.
nsrhoeos = 1
# Is the slope of the linear equation of state that relates fluid density to the height of the
#   pressure head (in terms of the reference density). note that drhodprhd can be calculated from
#   the volumetric expansion coefficient for pressure using equation 15. if the simulation is
#   formulated in terms of kilograms and meters, drhodprhd has an approximate value of 4.46 x 10-3
#   kg/m4. a value of zero, which is typically used for most problems, inactivates the dependence
#   of fluid density on pressure.
drhodprhd = 0.00446
# Is the reference pressure head. this value should normally be set to zero.
prhdref = 0.0

vdf = flopy.seawat.swtvdf.SeawatVdf(model=model, mtdnconc=mtdnconc, mfnadvfd=mfnadvfd,
                                    nswtcpl=nswtcpl, iwtable=iwtable, densemin=densemin,
                                    densemax=densemax, dnscrit=dnscrit, denseref=denseref,
                                    denseslp=denseslp, crhoref=crhoref, firstdt=firstdt,
                                    indense=indense, dense=dense, nsrhoeos=nsrhoeos,
                                    drhodprhd=drhodprhd, prhdref=prhdref)
```

## vsc


```python
# The model object (of type :class:`flopy.seawat.swt.seawat`) to which this package will be added.
model = seawat
mt3dmuflg = -1
# Is the minimum fluid viscosity. if the resulting viscosity value calculated with the equation is
#   less than viscmin, the viscosity value is set to viscmin. if viscmin = 0, the computed fluid
#   viscosity is not limited by viscmin (this is the option to use for most simulations). if
#   viscmin > 0, a computed fluid viscosity less than viscmin is automatically reset to viscmin.
viscmin = 0.0
# Is the maximum fluid viscosity. if the resulting viscosity value calculated with the equation is
#   greater than viscmax, the viscosity value is set to viscmax. if viscmax = 0, the computed fluid
#   viscosity is not limited by viscmax (this is the option to use for most simulations). if
#   viscmax > 0, a computed fluid viscosity larger than viscmax is automatically reset to viscmax.
viscmax = 0.0
# Is the fluid viscosity at the reference concentration and reference temperature. for most
#   simulations, viscref is specified as the viscosity of freshwater.
viscref = 0.0008904
nsmueos = 0
# Is a flag that specifies the option for including the effect of temperature on fluid viscosity.
#   if mutempopt = 0, the effect of temperature on fluid viscosity is not included or is a simple
#   linear relation that is specified in item 3c. if mutempopt = 1, fluid viscosity is calculated
#   using equation 18. the size of the amucoeff array in item 3e is 4 (muncoeff = 4). if mutempopt
#   = 2, fluid viscosity is calculated using equation 19. the size of the amucoeff array in item 3e
#   is 5 (muncoeff = 5). if mutempopt = 3, fluid viscosity is calculated using equation 20. the
#   size of the amucoeff array in item 3e is 2 (muncoeff = 2). if nsmueos and mutempopt are both
#   set to zero, all fluid viscosities are set to viscref.
mutempopt = 2
# Is the mt3dms species number corresponding to the adjacent dmudc and cmuref.
mtmuspec = 1
# Is the slope of the linear equation that relates fluid viscosity to solute concentration.
dmudc = 1.923e-06
# Is the reference concentration.
cmuref = 0.0
mtmutempspec = 1
# Is the coefficient array of size muncoeff. amucoeff is a in equations 18, 19, and 20.
amucoeff = [0.001, 1, 0.015512, -20.0, -1.572]
# Is a flag. invisc is read only if mt3dmuflg is equal to zero. if invisc < 0, values for the visc
#   array will be reused from the previous stress period. if it is the first stress period, values
#   for the visc array will be set to viscref. if invisc = 0, values for the visc array will be set
#   to viscref. if invisc >= 1, values for the visc array will be read from item 5. if invisc = 2,
#   values read for the visc array are assumed to represent solute concentration, and will be
#   converted to viscosity values.
invisc = -1
# Is the fluid viscosity array read for each layer using the modflow-2000 u2drel array reader. the
#   visc array is read only if mt3dmuflg is equal to zero. the visc array may also be entered in
#   terms of solute concen- tration (or any other units) if invisc is set to 2, and the simple
#   linear expression in item 3 can be used to represent the relation to viscosity.
visc = None

vsc = flopy.seawat.swtvsc.SeawatVsc(model=model, mt3dmuflg=mt3dmuflg, viscmin=viscmin,
                                    viscmax=viscmax, viscref=viscref, nsmueos=nsmueos,
                                    mutempopt=mutempopt, mtmuspec=mtmuspec, dmudc=dmudc,
                                    cmuref=cmuref, mtmutempspec=mtmutempspec, amucoeff=amucoeff,
                                    invisc=invisc, visc=visc)
```

# Run this thing!


```python
seawat.write_input()
# seawat.run_model()
```
