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
modelname = 'swttest'
namefile_ext = 'nam'
version = 'mf2005'
exe_name = 'mf2005.exe'
structured = True
listunit = 2
model_ws = '.'
external_path = None
verbose = False

modflow = flopy.modflow.mf.Modflow(modelname=modelname, namefile_ext=namefile_ext, version=version,
                                   exe_name=exe_name, structured=structured, listunit=listunit,
                                   model_ws=model_ws, external_path=external_path, verbose=verbose)
```

## zone


```python
model = modflow
zone_dict = None

zone = flopy.modflow.mfzon.ModflowZon(model=model, zone_dict=zone_dict)
```

## mult


```python
model = modflow
mult_dict = None

mult = flopy.modflow.mfmlt.ModflowMlt(model=model, mult_dict=mult_dict)
```

## pval


```python
model = modflow
pval_dict = None

pval = flopy.modflow.mfpval.ModflowPval(model=model, pval_dict=pval_dict)
```

## bas6


```python
model = modflow
ibound = np.array([])
strt = np.array([])
ifrefm = True
ixsec = False
ichflg = False
stoper = None
hnoflo = -999.99

bas6 = flopy.modflow.mfbas.ModflowBas(model=model, ibound=ibound, strt=strt, ifrefm=ifrefm,
                                      ixsec=ixsec, ichflg=ichflg, stoper=stoper, hnoflo=hnoflo)
```

## dis


```python
model = modflow
nlay = 1
nrow = 2
ncol = 2
nper = 1
delr = 1.0
delc = 1.0
laycbd = 0
top = 1.0
botm = 0.0
perlen = 1.0
nstp = 1
tsmult = 1.0
steady = True
itmuni = 4
lenuni = 2

dis = flopy.modflow.mfdis.ModflowDis(model=model, nlay=nlay, nrow=nrow, ncol=ncol, nper=nper,
                                     delr=delr, delc=delc, laycbd=laycbd, top=top, botm=botm,
                                     perlen=perlen, nstp=nstp, tsmult=tsmult, steady=steady,
                                     itmuni=itmuni, lenuni=lenuni)
```

## disu


```python
model = modflow
nodes = 2
nlay = 1
njag = None
ivsd = 0
nper = 1
itmuni = 4
lenuni = 2
idsymrd = 0
laycbd = 0
nodelay = None
top = 1
bot = 0
area = 1.0
iac = None
ja = None
ivc = None
cl1 = None
cl2 = None
cl12 = None
fahl = None
perlen = 1
nstp = 1
tsmult = 1
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
model = modflow
ipakcb = 0
intercellt = 0
laycon = 3
trpy = 1.0
hdry = -1e+30
iwdflg = 0
wetfct = 0.1
iwetit = 1
ihdwet = 0
tran = 1.0
hy = 1.0
vcont = None
sf1 = 9.999999747378752e-06
sf2 = 0.15000000596046448
wetdry = -0.009999999776482582

bcf6 = flopy.modflow.mfbcf.ModflowBcf(model=model, ipakcb=ipakcb, intercellt=intercellt,
                                      laycon=laycon, trpy=trpy, hdry=hdry, iwdflg=iwdflg,
                                      wetfct=wetfct, iwetit=iwetit, ihdwet=ihdwet, tran=tran,
                                      hy=hy, vcont=vcont, sf1=sf1, sf2=sf2, wetdry=wetdry)
```

## lpf


```python
model = modflow
laytyp = 0
layavg = 0
chani = 1.0
layvka = 0
laywet = 0
ipakcb = 0
hdry = -1e+30
iwdflg = 0
wetfct = 0.1
iwetit = 1
ihdwet = 0
hk = 1.0
hani = 1.0
vka = 1.0
ss = 9.999999747378752e-06
sy = 0.15000000596046448
vkcb = 0.0
wetdry = -0.009999999776482582
storagecoefficient = False
constantcv = False
thickstrt = False
nocvcorrection = False
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
model = modflow
nphfb = 0
mxfb = 0
nhfbnp = 0
hfb_data = None
nacthfb = 0
no_print = False
options = None

hfb6 = flopy.modflow.mfhfb.ModflowHfb(model=model, nphfb=nphfb, mxfb=mxfb, nhfbnp=nhfbnp,
                                      hfb_data=hfb_data, nacthfb=nacthfb, no_print=no_print,
                                      options=options)
```

## chd


```python
model = modflow
stress_period_data = {}
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('shead', '<f4'), ('ehead', '<f4')])
options = []

chd = flopy.modflow.mfchd.ModflowChd(model=model, stress_period_data=stress_period_data,
                                     dtype=dtype, options=options)
```

## fhb


```python
model = modflow
nbdtim = 1
nflw = 0
nhed = 0
ifhbss = 0
ipakcb = 0
nfhbx1 = 0
nfhbx2 = 0
ifhbpt = 0
bdtimecnstm = 1.0
bdtime = 0.0
cnstm5 = 1.0
ds5 = None
cnstm7 = 1.0
ds7 = None

fhb = flopy.modflow.mffhb.ModflowFhb(model=model, nbdtim=nbdtim, nflw=nflw, nhed=nhed,
                                     ifhbss=ifhbss, ipakcb=ipakcb, nfhbx1=nfhbx1, nfhbx2=nfhbx2,
                                     ifhbpt=ifhbpt, bdtimecnstm=bdtimecnstm, bdtime=bdtime,
                                     cnstm5=cnstm5, ds5=ds5, cnstm7=cnstm7, ds7=ds7)
```

## wel


```python
model = modflow
ipakcb = 0
stress_period_data = {}
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('flux', '<f4')])
options = []

wel = flopy.modflow.mfwel.ModflowWel(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     options=options)
```

## mnw2


```python
model = modflow
mnwmax = 0
nodtot = None
ipakcb = 0
mnwprnt = 0
aux = []
node_data = np.array([])
mnw = {}
stress_period_data = {0: rec.array([],            dtype=[('k', '<i8'), ('i', '<i8'), ('j', '<i8'),\
                     ('wellid', 'O'), ('qdes', '<f4'), ('capmult', '<i8'), ('cprime', '<f4'),\
                     ('hlim', '<f4'), ('qcut', '<i8'), ('qfrcmn', '<f4'), ('qfrcmx', '<f4')])}
itmp = []
gwt = False

mnw2 = flopy.modflow.mfmnw2.ModflowMnw2(model=model, mnwmax=mnwmax, nodtot=nodtot, ipakcb=ipakcb,
                                        mnwprnt=mnwprnt, aux=aux, node_data=node_data, mnw=mnw,
                                        stress_period_data=stress_period_data, itmp=itmp, gwt=gwt)
```

## mnwi


```python
model = modflow
wel1flag = None
qsumflag = None
byndflag = None
mnwobs = 1
wellid_unit_qndflag_qhbflag_concflag = None

mnwi = flopy.modflow.mfmnwi.ModflowMnwi(model=model, wel1flag=wel1flag, qsumflag=qsumflag,
                                        byndflag=byndflag, mnwobs=mnwobs,
                                        wellid_unit_qndflag_qhbflag_concflag=wellid_unit_qndflag_qhbflag_concflag)
```

## drn


```python
model = modflow
ipakcb = 0
stress_period_data = {}
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('elev', '<f4'), ('cond', '<f4')])
options = []

drn = flopy.modflow.mfdrn.ModflowDrn(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     options=options)
```

## rch


```python
model = modflow
nrchop = 3
ipakcb = 0
rech = 0.0010000000474974513
irch = None

rch = flopy.modflow.mfrch.ModflowRch(model=model, nrchop=nrchop, ipakcb=ipakcb, rech=rech,
                                     irch=irch)
```

## evt


```python
model = modflow
nevtop = 3
ipakcb = 0
surf = 0.0
evtr = 0.0010000000474974513
exdp = 1.0
ievt = 1
external = True

evt = flopy.modflow.mfevt.ModflowEvt(model=model, nevtop=nevtop, ipakcb=ipakcb, surf=surf,
                                     evtr=evtr, exdp=exdp, ievt=ievt, external=external)
```

## ghb


```python
model = modflow
ipakcb = 0
stress_period_data = {}
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('bhead', '<f4'), ('cond', '<f4')])
no_print = False
options = []

ghb = flopy.modflow.mfghb.ModflowGhb(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     no_print=no_print, options=options)
```

## gmg


```python
model = modflow
mxiter = 50
iiter = 30
iadamp = 0
hclose = 1e-05
rclose = 1e-05
relax = 1.0
ioutgmg = 0
iunitmhc = 0
ism = 0
isc = 0
damp = 1.0
dup = 0.75
dlow = 0.01
chglimit = 1.0

gmg = flopy.modflow.mfgmg.ModflowGmg(model=model, mxiter=mxiter, iiter=iiter, iadamp=iadamp,
                                     hclose=hclose, rclose=rclose, relax=relax, ioutgmg=ioutgmg,
                                     iunitmhc=iunitmhc, ism=ism, isc=isc, damp=damp, dup=dup,
                                     dlow=dlow, chglimit=chglimit)
```

## lmt6


```python
model = modflow
output_file_name = 'mt3d_link.ftl'
output_file_unit = 54
output_file_header = 'extended'
output_file_format = 'unformatted'
package_flows = []

lmt6 = flopy.modflow.mflmt.ModflowLmt(model=model, output_file_name=output_file_name,
                                      output_file_unit=output_file_unit,
                                      output_file_header=output_file_header,
                                      output_file_format=output_file_format,
                                      package_flows=package_flows)
```

## lmt7


```python
model = modflow
output_file_name = 'mt3d_link.ftl'
output_file_unit = 54
output_file_header = 'extended'
output_file_format = 'unformatted'
package_flows = []

lmt7 = flopy.modflow.mflmt.ModflowLmt(model=model, output_file_name=output_file_name,
                                      output_file_unit=output_file_unit,
                                      output_file_header=output_file_header,
                                      output_file_format=output_file_format,
                                      package_flows=package_flows)
```

## riv


```python
model = modflow
ipakcb = 0
stress_period_data = {}
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('stage', '<f4'), ('cond', '<f4'),
        ('rbot', '<f4')])
options = []

riv = flopy.modflow.mfriv.ModflowRiv(model=model, ipakcb=ipakcb,
                                     stress_period_data=stress_period_data, dtype=dtype,
                                     options=options)
```

## str


```python
model = modflow
mxacts = 0
nss = 0
ntrib = 0
ndiv = 0
icalc = 0
const = 86400.0
ipakcb = 0
istcb2 = None
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('segment', '<i8'), ('reach', '<i8'),
        ('flow', '<f4'), ('stage', '<f4'), ('cond', '<f4'), ('sbot', '<f4'), ('stop', '<f4'),
        ('width', '<f4'), ('slope', '<f4'), ('rough', '<f4')])
stress_period_data = {}
segment_data = None
options = []

str = flopy.modflow.mfstr.ModflowStr(model=model, mxacts=mxacts, nss=nss, ntrib=ntrib, ndiv=ndiv,
                                     icalc=icalc, const=const, ipakcb=ipakcb, istcb2=istcb2,
                                     dtype=dtype, stress_period_data=stress_period_data,
                                     segment_data=segment_data, options=options)
```

## swi2


```python
model = modflow
nsrf = 1
istrat = 1
nobs = 0
iswizt = 0
ipakcb = 0
iswiobs = 0
options = None
nsolver = 1
iprsol = 0
mutsol = 3
solver2params = {'damp': 1.0, 'rclose': 0.0001, 'relax': 1.0, 'zclose': 0.001}
toeslope = 0.05
tipslope = 0.05
alpha = None
beta = 0.1
nadptmx = 1
nadptmn = 1
adptfct = 1.0
nu = 0.02500000037252903
zeta = 0.0
ssz = 0.25
isource = 0
obsnam = None
obslrc = None
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
model = modflow
mxiter = 50
iter1 = 30
npcond = 1
hclose = 1e-05
rclose = 1e-05
relax = 1.0
nbpol = 0
iprpcg = 0
mutpcg = 3
damp = 1.0
dampt = 1.0
ihcofadd = 0

pcg = flopy.modflow.mfpcg.ModflowPcg(model=model, mxiter=mxiter, iter1=iter1, npcond=npcond,
                                     hclose=hclose, rclose=rclose, relax=relax, nbpol=nbpol,
                                     iprpcg=iprpcg, mutpcg=mutpcg, damp=damp, dampt=dampt,
                                     ihcofadd=ihcofadd)
```

## pcgn


```python
model = modflow
iter_mo = 50
iter_mi = 30
close_r = 1e-05
close_h = 1e-05
relax = 1.0
ifill = 0
unit_pc = 0
unit_ts = 0
adamp = 0
damp = 1.0
damp_lb = 0.001
rate_d = 0.1
chglimit = 0.0
acnvg = 0
cnvg_lb = 0.001
mcnvg = 2
rate_c = -1.0
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
model = modflow
headtol = 0.01
fluxtol = 500
maxiterout = 100
thickfact = 1e-05
linmeth = 1
iprnwt = 0
ibotav = 0
options = 'COMPLEX'
Continue = False
dbdtheta = 0.4
dbdkappa = 1e-05
dbdgamma = 0.0
momfact = 0.1
backflag = 1
maxbackiter = 50
backtol = 1.1
backreduce = 0.7
maxitinner = 50
ilumethod = 2
levfill = 5
stoptol = 1e-10
msdr = 15
iacl = 2
norder = 1
level = 5
north = 7
iredsys = 0
rrctols = 0.0
idroptol = 1
epsrn = 0.0001
hclosexmd = 0.0001
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
model = modflow
mxiter = 100
innerit = 50
isolver = 1
npc = 2
iscl = 0
iord = 0
ncoresm = 1
ncoresv = 1
damp = 1.0
dampt = 1.0
relax = 0.97
ifill = 0
droptol = 0.0
hclose = 0.001
rclose = 0.1
l2norm = None
iprpks = 0
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
model = modflow
hclose = 0.0001
hiclose = 0.0001
mxiter = 100
iter1 = 20
iprsms = 2
nonlinmeth = 0
linmeth = 2
theta = 0.7
akappa = 0.1
gamma = 0.2
amomentum = 0.001
numtrack = 20
btol = 10000.0
breduc = 0.2
reslim = 100.0
iacl = 2
norder = 0
level = 7
north = 2
iredsys = 0
rrctol = 0.0
idroptol = 0
epsrn = 0.001
clin = 'bcgs'
ipc = 3
iscl = 0
iord = 0
rclosepcgu = 0.1
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
options = None

lak = flopy.modflow.mflak.ModflowLak(model=model, nlakes=nlakes, ipakcb=ipakcb, theta=theta,
                                     nssitr=nssitr, sscncr=sscncr, surfdep=surfdep, stages=stages,
                                     stage_range=stage_range, tab_files=tab_files,
                                     tab_units=tab_units, lakarr=lakarr, bdlknc=bdlknc,
                                     sill_data=sill_data, flux_data=flux_data, options=options)
```

## gage


```python
model = modflow
numgage = 0
gage_data = None
files = None

gage = flopy.modflow.mfgage.ModflowGage(model=model, numgage=numgage, gage_data=gage_data,
                                        files=files)
```

## sip


```python
model = modflow
mxiter = 200
nparm = 5
accl = 1
hclose = 1e-05
ipcalc = 1
wseed = 0
iprsip = 0

sip = flopy.modflow.mfsip.ModflowSip(model=model, mxiter=mxiter, nparm=nparm, accl=accl,
                                     hclose=hclose, ipcalc=ipcalc, wseed=wseed, iprsip=iprsip)
```

## sor


```python
model = modflow
mxiter = 200
accl = 1
hclose = 1e-05
iprsor = 0

sor = flopy.modflow.mfsor.ModflowSor(model=model, mxiter=mxiter, accl=accl, hclose=hclose,
                                     iprsor=iprsor)
```

## de4


```python
model = modflow
itmx = 50
mxup = 0
mxlow = 0
mxbw = 0
ifreq = 3
mutd4 = 0
accl = 1.0
hclose = 1e-05
iprd4 = 1

de4 = flopy.modflow.mfde4.ModflowDe4(model=model, itmx=itmx, mxup=mxup, mxlow=mxlow, mxbw=mxbw,
                                     ifreq=ifreq, mutd4=mutd4, accl=accl, hclose=hclose,
                                     iprd4=iprd4)
```

## oc


```python
model = modflow
ihedfm = 0
iddnfm = 0
chedfm = None
cddnfm = None
cboufm = None
compact = True
stress_period_data = {(0, 0): ['save head']}

oc = flopy.modflow.mfoc.ModflowOc(model=model, ihedfm=ihedfm, iddnfm=iddnfm, chedfm=chedfm,
                                  cddnfm=cddnfm, cboufm=cboufm, compact=compact,
                                  stress_period_data=stress_period_data)
```

## uzf


```python
model = modflow
nuztop = 1
iuzfopt = 0
irunflg = 0
ietflg = 0
ipakcb = 0
iuzfcb2 = 0
ntrail2 = 10
nsets = 20
nuzgag = 0
surfdep = 1.0
iuzfbnd = 1
irunbnd = 0
vks = 9.999999974752427e-07
eps = 3.5
thts = 0.35
thtr = 0.15
thti = 0.2
specifythtr = 0
specifythti = 0
nosurfleak = 0
finf = 9.99999993922529e-09
pet = 5e-08
extdp = 15.0
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
model = modflow
laytyp = 0
layavg = 0
chani = 1.0
layvka = 0
laywet = 0
ipakcb = None
hdry = -1e+30
iphdry = 0
hk = 1.0
hani = 1.0
vka = 1.0
ss = 1e-05
sy = 0.15
vkcb = 0.0
noparcheck = False

upw = flopy.modflow.mfupw.ModflowUpw(model=model, laytyp=laytyp, layavg=layavg, chani=chani,
                                     layvka=layvka, laywet=laywet, ipakcb=ipakcb, hdry=hdry,
                                     iphdry=iphdry, hk=hk, hani=hani, vka=vka, ss=ss, sy=sy,
                                     vkcb=vkcb, noparcheck=noparcheck)
```

## sub


```python
model = modflow
ipakcb = 0
isuboc = 0
idsave = None
idrest = 0
nndb = 1
ndb = 1
nmz = 1
nn = 20
ac1 = 0.0
ac2 = 0.2
itmin = 5
ln = 0
ldn = 0
rnb = 1.0
hc = 100000.0
sfe = 9.999999747378752e-05
sfv = 0.0010000000474974513
com = 0.0
dp = np.array([ 0.000001, 0.000006, 0.0006 ])
dstart = 1.0
dhc = 100000.0
dcom = 0.0
dz = 1.0
nz = 1
ids15 = None
ids16 = None

sub = flopy.modflow.mfsub.ModflowSub(model=model, ipakcb=ipakcb, isuboc=isuboc, idsave=idsave,
                                     idrest=idrest, nndb=nndb, ndb=ndb, nmz=nmz, nn=nn, ac1=ac1,
                                     ac2=ac2, itmin=itmin, ln=ln, ldn=ldn, rnb=rnb, hc=hc, sfe=sfe,
                                     sfv=sfv, com=com, dp=dp, dstart=dstart, dhc=dhc, dcom=dcom,
                                     dz=dz, nz=nz, ids15=ids15, ids16=ids16)
```

## swt


```python
model = modflow
ipakcb = 0
iswtoc = 0
nsystm = 1
ithk = 0
ivoid = 0
istpcs = 1
icrcc = 0
lnwt = 0
izcfl = 0
izcfm = 0
iglfl = 0
iglfm = 0
iestfl = 0
iestfm = 0
ipcsfl = 0
ipcsfm = 0
istfl = 0
istfm = 0
gl0 = 0.0
sgm = 1.7000000476837158
sgs = 2.0
thick = 1.0
sse = None
ssv = None
cr = 0.009999999776482582
cc = 0.25
void = 0.8199999928474426
sub = 0.0
pcsoff = 0.0
pcs = None
ids16 = None
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
model = modflow
nhyd = 1
ihydun = 536
hydnoh = -999.0
obsdata = (b'BAS', b'HD', b'I', 1, 0.0, 0.0, b'HOBS1')

hyd = flopy.modflow.mfhyd.ModflowHyd(model=model, nhyd=nhyd, ihydun=ihydun, hydnoh=hydnoh,
                                     obsdata=obsdata)
```

## hob


```python
model = modflow
iuhobsv = 0
hobdry = 0
tomulth = 1.0
obs_data = None
hobname = None

hob = flopy.modflow.mfhob.ModflowHob(model=model, iuhobsv=iuhobsv, hobdry=hobdry, tomulth=tomulth,
                                     obs_data=obs_data, hobname=hobname)
```

## flopy.mt3d


```python
modelname = 'swttest'
namefile_ext = 'nam'
modflowmodel = modflow
ftlfilename = None
version = 'mt3dms'
exe_name = 'mt3dms.exe'
structured = True
listunit = None
model_ws = '.'
external_path = None
verbose = False
load = True
silent = 0

mt3d = flopy.mt3d.mt.Mt3dms(modelname=modelname, namefile_ext=namefile_ext,
                            modflowmodel=modflowmodel, ftlfilename=ftlfilename, version=version,
                            exe_name=exe_name, structured=structured, listunit=listunit,
                            model_ws=model_ws, external_path=external_path, verbose=verbose,
                            load=load, silent=silent)
```

## btn


```python
model = mt3d
nlay = 1
nrow = 2
ncol = 2
nper = 1
ncomp = 1
mcomp = 1
tunit = 'D'
lunit = 'M'
munit = 'KG'
laycon = 3
delr = 1.0
delc = 1.0
htop = 1.0
dz = 1.0
prsity = 0.30000001192092896
icbund = 1
sconc = 0.0
cinact = 1e+30
thkmin = 0.01
ifmtcn = 0
ifmtnp = 0
ifmtrf = 0
ifmtdp = 0
savucn = True
nprs = 0
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
model = mt3d
mixelm = 3
percel = 0.75
mxpart = 800000
nadvfd = 1
itrack = 3
wd = 0.5
dceps = 1e-05
nplane = 2
npl = 10
nph = 40
npmin = 5
npmax = 80
nlsink = 0
npsink = 15
dchmoc = 0.0001

adv = flopy.mt3d.mtadv.Mt3dAdv(model=model, mixelm=mixelm, percel=percel, mxpart=mxpart,
                               nadvfd=nadvfd, itrack=itrack, wd=wd, dceps=dceps, nplane=nplane,
                               npl=npl, nph=nph, npmin=npmin, npmax=npmax, nlsink=nlsink,
                               npsink=npsink, dchmoc=dchmoc)
```

## dsp


```python
model = mt3d
al = 0.009999999776482582
trpt = 0.10000000149011612
trpv = 0.009999999776482582
dmcoef = 9.999999717180685e-10
multiDiff = False

dsp = flopy.mt3d.mtdsp.Mt3dDsp(model=model, al=al, trpt=trpt, trpv=trpv, dmcoef=dmcoef,
                               multiDiff=multiDiff)
```

## ssm


```python
model = mt3d
crch = None
cevt = None
mxss = 8
stress_period_data = None
dtype = np.dtype([('k', '<i8'), ('i', '<i8'), ('j', '<i8'), ('css', '<f4'), ('itype', '<i8')])

ssm = flopy.mt3d.mtssm.Mt3dSsm(model=model, crch=crch, cevt=cevt, mxss=mxss,
                               stress_period_data=stress_period_data, dtype=dtype)
```

## rct


```python
model = mt3d
isothm = 0
ireact = 0
igetsc = 1
rhob = 1800.0
prsity2 = 0.10000000149011612
srconc = 0.0
sp1 = 0.0
sp2 = 0.0
rc1 = 0.0
rc2 = 0.0

rct = flopy.mt3d.mtrct.Mt3dRct(model=model, isothm=isothm, ireact=ireact, igetsc=igetsc, rhob=rhob,
                               prsity2=prsity2, srconc=srconc, sp1=sp1, sp2=sp2, rc1=rc1, rc2=rc2)
```

## gcg


```python
model = mt3d
mxiter = 1
iter1 = 50
isolve = 3
ncrs = 0
accl = 1
cclose = 1e-05
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
model = mt3d
nlkinit = 0
mxlkbc = 0
icbclk = None
ietlak = 0
coldlak = 0.0
lk_stress_period_data = None
dtype = None

lkt = flopy.mt3d.mtlkt.Mt3dLkt(model=model, nlkinit=nlkinit, mxlkbc=mxlkbc, icbclk=icbclk,
                               ietlak=ietlak, coldlak=coldlak,
                               lk_stress_period_data=lk_stress_period_data, dtype=dtype)
```

## sft


```python
model = mt3d
nsfinit = 0
mxsfbc = 0
icbcsf = 0
ioutobs = None
ietsfr = 0
isfsolv = 1
wimp = 0.5
wups = 1.0
cclosesf = 1e-06
mxitersf = 10
crntsf = 1.0
iprtxmd = 0
coldsf = 0.0
dispsf = 0.0
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
model = mt3d
mxuzcon = 0
icbcuz = None
iet = 0
iuzfbnd = None
wc = 0.0
sdh = 0.0
cuzinf = None
cuzet = None
cgwet = None

uzt = flopy.mt3d.mtuzt.Mt3dUzt(model=model, mxuzcon=mxuzcon, icbcuz=icbcuz, iet=iet,
                               iuzfbnd=iuzfbnd, wc=wc, sdh=sdh, cuzinf=cuzinf, cuzet=cuzet,
                               cgwet=cgwet)
```

## flopy.seawat


```python
modelname = 'swttest'
namefile_ext = 'nam'
modflowmodel = modflow
mt3dmodel = mt3d
version = 'seawat'
exe_name = 'swt_v4'
structured = True
listunit = 2
model_ws = '.'
external_path = None
verbose = False
load = True
silent = 0

seawat = flopy.seawat.swt.Seawat(modelname=modelname, namefile_ext=namefile_ext,
                                 modflowmodel=modflowmodel, mt3dmodel=mt3dmodel, version=version,
                                 exe_name=exe_name, structured=structured, listunit=listunit,
                                 model_ws=model_ws, external_path=external_path, verbose=verbose,
                                 load=load, silent=silent)
```

## vdf


```python
model = seawat
mtdnconc = 1
mfnadvfd = 1
nswtcpl = 1
iwtable = 1
densemin = 1.0
densemax = 1.025
dnscrit = 0.01
denseref = 1.0
denseslp = 0.025
crhoref = 0
firstdt = 0.001
indense = 1
dense = None
nsrhoeos = 1
drhodprhd = 0.00446
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
model = seawat
mt3dmuflg = -1
viscmin = 0.0
viscmax = 0.0
viscref = 0.0008904
nsmueos = 0
mutempopt = 2
mtmuspec = 1
dmudc = 1.923e-06
cmuref = 0.0
mtmutempspec = 1
amucoeff = [0.001, 1, 0.015512, -20.0, -1.572]
invisc = -1
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
