from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

import os

pvPrefix = os.environ['PV_HOME']
dataPrefix = '/scratch/01237/bloring/striped/kh-jaguar-new/'

batch=1 # commnad line run
pvpy=1  # pvpython or pvbatch
rc=1

time=float(os.environ['PV_TIME'])
outputImage='kh-new-jaguar-lic-b-woce.%d.png'%(int(time))
logfile=os.environ['PV_LOGFILE']

if batch:
  if pvpy:
    if rc:
      ReverseConnect(os.environ['PV_PORT'])
    else:
      Connect('localhost',11111)

  LICPlugin = '%s/lib/libSurfaceLIC.so'%(pvPrefix)
  LoadPlugin(LICPlugin, False, globals())
  LoadPlugin(LICPlugin, True, globals())

  SQPlugin = '%s/lib/libSciberQuestToolKit.so'%(pvPrefix)
  LoadPlugin(SQPlugin, False, globals())
  LoadPlugin(SQPlugin, True, globals())

# reader
inputData='%s/jaguar.bov'%(dataPrefix)
r = SQBOVReader(FileName=inputData)
r.CollectBufferSize=' 512 MB'
#r.FileName='/scratch1/scratchdirs/loring/striped/kh-new-jaguar/jaguar.bov'
r.ISubset=[700, 7491]
r.JSubset=[0, 16383]
r.KSubset=[0, 0]
#r.ISubsetInfo=[0, 8191]
#r.JSubsetInfo=[0, 16383]
#r.KSubsetInfo=[0, 0]
r.NumberOfIONodes=0
r.Arrays=['B', 'Ue']
#r.PointArrayInfo=['B', '1', 'Bx', '0', 'By', '0', 'Bz', '0', 'Ue', '1', 'Uex', '0', 'Uey', '0', 'Uez', '0']
r.SieveBufferSize='default'
#r.TimestepValues=[0.0, 4728.0, 9456.0, 14184.0, 18912.0, 23640.0, 28368.0, 33096.0, 37824.0, 42552.0, 47280.0, 52008.0, 56736.0, 61464.0, 66192.0, 70920.0, 75648.0, 80376.0, 85104.0, 89832.0, 94560.0, 99288.0, 104016.0, 108744.0, 113472.0, 118200.0, 122928.0, 127656.0, 132384.0, 137112.0, 141840.0, 146568.0, 151296.0, 156024.0, 160752.0, 165480.0, 170208.0, 174936.0, 179664.0, 184392.0, 189120.0, 193848.0, 198576.0, 203304.0, 208032.0, 212760.0, 217488.0, 222216.0, 226944.0, 231672.0, 236400.0, 241128.0, 245856.0, 250584.0, 255312.0, 260040.0, 264768.0, 269496.0, 274224.0, 278952.0, 283680.0, 288408.0, 293136.0, 297864.0, 302592.0, 307320.0, 312048.0, 316776.0, 321504.0, 326232.0, 330960.0, 335688.0, 340416.0, 345144.0, 349872.0, 354600.0, 359328.0, 364056.0, 368784.0, 373512.0, 378240.0, 382968.0, 387696.0, 392424.0, 397152.0, 401880.0, 406608.0, 411336.0, 416064.0, 420792.0, 425520.0, 430248.0, 434976.0, 439704.0, 444432.0, 449160.0, 453888.0, 458616.0, 463344.0, 468072.0, 472800.0, 477528.0, 482256.0, 486984.0, 491712.0, 496440.0, 501168.0, 505896.0, 510624.0, 515352.0, 520080.0, 524808.0, 529536.0, 534264.0, 538992.0, 543720.0, 548448.0, 553176.0, 557904.0, 562632.0, 567360.0, 572088.0, 576816.0, 581544.0, 586272.0, 591000.0, 595728.0, 600456.0, 605184.0, 609912.0, 614640.0, 619368.0, 624096.0, 628824.0, 633552.0, 638280.0, 643008.0, 647736.0, 652464.0, 657192.0, 661920.0, 666648.0, 671376.0, 676104.0, 680832.0, 685560.0, 690288.0, 695016.0, 699744.0, 704472.0, 709200.0, 713928.0, 718656.0, 723384.0, 728112.0, 732840.0, 737568.0, 742296.0, 747024.0, 751752.0, 756480.0, 761208.0, 765936.0, 770664.0, 775392.0, 780120.0, 784848.0, 789576.0, 794304.0, 799032.0, 803760.0, 808488.0, 813216.0, 817944.0, 822672.0, 827400.0, 832128.0, 836856.0, 841584.0, 846312.0, 851040.0, 855768.0, 860496.0, 865224.0, 869952.0, 874680.0, 879408.0, 884136.0, 888864.0, 893592.0, 898320.0, 903048.0, 907776.0, 912504.0, 917232.0, 921960.0, 926688.0, 931416.0, 936144.0, 940872.0, 945600.0, 950328.0, 955056.0, 959784.0, 964512.0, 969240.0, 973968.0, 978696.0, 983424.0, 988152.0, 992880.0, 997608.0, 1002336.0, 1007064.0, 1011792.0, 1016520.0, 1021248.0, 1025976.0, 1030704.0, 1035432.0, 1040160.0, 1044888.0, 1049616.0, 1054344.0, 1059072.0, 1063800.0, 1068528.0, 1073256.0, 1077984.0, 1082712.0, 1087440.0, 1092168.0, 1096896.0, 1101624.0, 1106352.0, 1111080.0, 1115808.0, 1120536.0, 1125264.0, 1129992.0, 1134720.0, 1139448.0, 1144176.0, 1148904.0, 1153632.0, 1158360.0, 1163088.0, 1167816.0, 1172544.0, 1177272.0, 1182000.0, 1186728.0, 1191456.0, 1196184.0, 1200912.0, 1205640.0, 1210368.0, 1215096.0, 1219824.0, 1224552.0, 1229280.0, 1234008.0, 1238736.0, 1243464.0, 1248192.0, 1252920.0, 1257648.0, 1262376.0, 1267104.0, 1271832.0, 1276560.0, 1281288.0, 1286016.0, 1290744.0, 1295472.0, 1300200.0, 1304928.0, 1309656.0, 1314384.0, 1319112.0, 1323840.0, 1328568.0, 1333296.0, 1338024.0, 1342752.0, 1347480.0, 1352208.0, 1356936.0, 1361664.0, 1366392.0, 1371120.0, 1375848.0, 1380576.0, 1385304.0, 1390032.0, 1394760.0, 1399488.0, 1404216.0, 1408944.0, 1413672.0, 1418400.0, 1423128.0, 1427856.0, 1432584.0, 1437312.0, 1442040.0, 1446768.0, 1451496.0, 1456224.0, 1460952.0, 1465680.0, 1470408.0, 1475136.0, 1479864.0, 1484592.0, 1489320.0, 1494048.0, 1498776.0, 1503504.0, 1508232.0, 1512960.0, 1517688.0, 1522416.0, 1527144.0, 1531872.0, 1536600.0, 1541328.0, 1546056.0, 1550784.0, 1555512.0, 1560240.0, 1564968.0, 1569696.0, 1574424.0, 1579152.0, 1583880.0, 1588608.0, 1593336.0, 1598064.0, 1602792.0, 1607520.0, 1612248.0, 1616976.0, 1621704.0, 1626432.0, 1631160.0, 1635888.0, 1640616.0, 1645344.0, 1650072.0, 1654800.0, 1659528.0, 1664256.0, 1668984.0, 1673712.0, 1678440.0, 1683168.0, 1687896.0, 1692624.0, 1697352.0, 1702080.0, 1706808.0, 1711536.0, 1716264.0, 1720992.0, 1725720.0, 1730448.0, 1735176.0, 1739904.0, 1744632.0, 1749360.0, 1754088.0, 1758816.0, 1763544.0, 1768272.0, 1773000.0, 1777728.0, 1782456.0, 1787184.0, 1791912.0, 1796640.0, 1801368.0, 1806096.0, 1810824.0, 1815552.0, 1820280.0, 1825008.0, 1829736.0, 1834464.0, 1839192.0, 1843920.0, 1848648.0, 1853376.0, 1858104.0, 1862832.0, 1867560.0, 1872288.0, 1877016.0, 1881744.0, 1886472.0, 1891200.0, 1895928.0, 1900656.0, 1905384.0, 1910112.0, 1914840.0, 1919568.0, 1924296.0, 1929024.0, 1933752.0, 1938480.0, 1943208.0, 1947936.0, 1952664.0, 1957392.0, 1962120.0, 1966848.0, 1971576.0, 1976304.0, 1981032.0, 1985760.0, 1990488.0, 1995216.0, 1999944.0, 2004672.0, 2009400.0, 2014128.0, 2018856.0, 2023584.0, 2028312.0, 2033040.0, 2037768.0, 2042496.0, 2047224.0, 2051952.0, 2056680.0, 2061408.0, 2066136.0, 2070864.0, 2075592.0, 2080320.0, 2085048.0, 2089776.0, 2094504.0, 2099232.0, 2103960.0, 2108688.0, 2113416.0, 2118144.0, 2122872.0, 2127600.0, 2132328.0, 2137056.0, 2141784.0, 2146512.0, 2151240.0, 2155968.0, 2160696.0, 2165424.0, 2170152.0, 2174880.0, 2179608.0, 2184336.0, 2189064.0, 2193792.0, 2198520.0, 2203248.0, 2207976.0, 2212704.0, 2217432.0, 2222160.0, 2226888.0, 2231616.0, 2236344.0, 2241072.0, 2245800.0, 2250528.0, 2255256.0, 2259984.0, 2264712.0, 2269440.0, 2274168.0, 2278896.0, 2283624.0, 2288352.0, 2293080.0, 2297808.0, 2302536.0, 2307264.0, 2311992.0, 2316720.0, 2321448.0, 2326176.0, 2330904.0, 2335632.0, 2340360.0, 2345088.0, 2349816.0, 2354544.0, 2359272.0, 2364000.0, 2368728.0, 2373456.0, 2378184.0, 2382912.0, 2387640.0, 2392368.0, 2397096.0]
r.UseCollectiveIO='enabled'
r.UseDataSieving='disabled'
r.UseDeferredOpen='automatic'
r.UseDirectIO='disabled'
r.VectorProjection='None'

# anim
asc = GetAnimationScene()
asc.AnimationTime = time

#view
view = GetRenderView()
view.AlphaBitPlanes=1
view.BackLightAzimuth=110.0
view.BackLightElevation=0.0
view.BackLightKBRatio=3.5
view.BackLightWarmth=0.5
view.Background=[0.31999694819562063, 0.3400015259021897, 0.4299992370489052]
view.Background2=[0.0, 0.0, 0.165]
#view.BackgroundTexture=None
#view.CacheKey=1512960.0
#view.Camera2DManipulators=[<paraview.servermanager.TrackballPan1 object at 0x8dc9890>, <paraview.servermanager.TrackballRoll object at 0x8dc9050>, <paraview.servermanager.TrackballZoom object at 0x8dc9a90>, <paraview.servermanager.TrackballZoom object at 0x8dc9f90>, <paraview.servermanager.TrackballZoom object at 0x8e856d0>, <paraview.servermanager.TrackballZoom object at 0x8e85590>, <paraview.servermanager.TrackballRoll object at 0x8e85610>, <paraview.servermanager.TrackballPan1 object at 0x8e85890>, <paraview.servermanager.TrackballRotate object at 0x8e854d0>]
#view.Camera3DManipulators=[<paraview.servermanager.TrackballRotate object at 0x8dc9f90>, <paraview.servermanager.TrackballPan1 object at 0x8dc9090>, <paraview.servermanager.TrackballZoom object at 0x8dc9050>, <paraview.servermanager.TrackballRoll object at 0x8dc9a90>, <paraview.servermanager.TrackballRotate object at 0x8e854d0>, <paraview.servermanager.TrackballPan1 object at 0x8e85910>, <paraview.servermanager.TrackballZoom object at 0x8e85450>, <paraview.servermanager.TrackballRotate object at 0x8e858d0>, <paraview.servermanager.TrackballZoom object at 0x8e85590>]
view.CenterAxesVisibility=0
view.CenterOfRotation=[4095.5, 8191.5, 0.0]
view.CollectGeometryThreshold=100.0
view.CompressorConfig='vtkSquirtCompressor 0 3'
view.DepthPeeling=1
view.FillLightAzimuth=-10.0
view.FillLightElevation=-75.0
view.FillLightKFRatio=3.0
view.FillLightWarmth=0.4
view.HeadLightKHRatio=3.0
view.HeadLightWarmth=0.5
#view.HiddenProps=[]
#view.HiddenRepresentations=[]
view.ImageReductionFactor=2
view.InteractionMode='2D'
view.KeyLightAzimuth=10.0
view.KeyLightElevation=50.0
view.KeyLightIntensity=0.75
view.KeyLightWarmth=0.6
view.LODResolution=0.5
view.LODThreshold=0.0
view.LightAmbientColor=[1.0, 1.0, 1.0]
view.LightDiffuseColor=[1.0, 1.0, 1.0]
view.LightIntensity=1.0
view.LightSpecularColor=[1.0, 1.0, 1.0]
view.LightSwitch=0
view.LightType='HeadLight'
view.MaintainLuminance=0
view.MaximumNumberOfPeels=4
view.MultiSamples=0
view.NonInteractiveRenderDelay=0.0
view.OrientationAxesInteractivity=0
view.OrientationAxesLabelColor=[1.0, 1.0, 1.0]
view.OrientationAxesOutlineColor=[1.0, 1.0, 1.0]
view.OrientationAxesVisibility=1
view.RemoteRenderThreshold=0.0
#view.Representations=[<paraview.servermanager.UniformGridRepresentation object at 0x8e85590>, <paraview.servermanager.UniformGridRepresentation object at 0x8e855d0>, <paraview.servermanager.UniformGridRepresentation object at 0x8e85890>, <paraview.servermanager.UniformGridRepresentation object at 0x8e95d50>, <paraview.servermanager.UniformGridRepresentation object at 0x8e85510>]
#view.ResetCamera=Property name= ResetCamera
view.StencilCapable=1
view.StereoCapableWindow=1
view.StereoRender=0
view.StereoType='Red-Blue'
view.StillRenderImageReductionFactor=1
view.UseCache=0
view.UseGradientBackground=0
view.UseInteractiveRenderingForSceenshots=0
view.UseLight=1
view.UseOffscreenRendering=0
view.UseOffscreenRenderingForScreenshots=0
view.UseOutlineForLODRendering=1
view.UseTexturedBackground=0
view.ViewPosition=[0, 0]
view.ViewSize=[2500, 1050]
view.ViewTime=time
view.CameraClippingRange=[35005.307206233374, 35889.279610431186]
#view.CameraClippingRangeInfo=[35005.307206233374, 35889.279610431186]
view.CameraFocalPoint=[4095.5, 8191.5, 0.0]
#view.CameraFocalPointInfo=[4095.5, 8191.5, 0.0]
view.CameraParallelProjection=0
view.CameraParallelScale=3515.179672114515
#view.CameraParallelScaleInfo=3515.179672114515
view.CameraPosition=[4095.5, 8191.5, -35358.8961679125]
#view.CameraPositionInfo=[4095.5, 8191.5, -35358.8961679125]
view.CameraViewAngle=30.0
view.CameraViewUp=[1.0, 0.0, 0.0]
#view.CameraViewUpInfo=[1.0, 0.0, 0.0]
view.EyeAngle=2.0
#view.EyeTransformMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
#view.ModelTransformMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

rep = Show(r)
rep.Representation = 'Outline'
Render()

# ig1
ig1 = SQImageGhosts()
ig1.Copyselectedarrays=[]
ig1.Copyallarrays=1
#Input=<paraview.servermanager.SQBOVReader object at 0x56d2390>

rep = Show(ig1)
rep.Representation = 'Outline'
Render()

# kc
kc = SQKernelConvolution()
kc.Arraystocopy=[]
kc.Arrays=['B', 'Ue']
kc.CPUOptimization='Minimize cache misses'
kc.ComputeResidual=0
#kc.Input=<paraview.servermanager.SQImageGhosts object at 0x8dc9ad0>
kc.KernelType='Gaussian'
kc.Width='15'

rep = Show(kc)
rep.Representation = 'Outline'
Render()

# ig2
ig2 = SQImageGhosts()
ig2.Copyselectedarrays=[]
ig2.Copyallarrays=1
#ig2.Input=<paraview.servermanager.SQKernelConvolution object at 0x8dbbf90>

rep = Show(ig2)
rep.Representation = 'Outline'
Render()

# vf
vf = SQVortexFilter()
vf.Arraystocopy=['B', 'Ue']
vf.Arrays=['Ue']
vf.Divergence=0
vf.Eigenvaluediagnostic=0
vf.Gradient=0
vf.Billsdiagnostic=0
vf.Helicity=0
vf.Lambda123=0
vf.Lambda2=0
vf.Normalizedhelicity=0
vf.Q=0
vf.Rotation=1
#vf.Input=<paraview.servermanager.SQImageGhosts object at 0x8e85250>
vf.Resultmagnitude=1
vf.Splitcomponents=0

rep = Show(vf)
rep.Representation = 'Outline'
Render()

# lut B
lut = GetLookupTableForArray('mag-rot-Ue',1)
lut.AllowDuplicateScalars=1
lut.Annotations=[]
#lut.Build=Property name= Build
lut.ColorSpace='Lab'
lut.Discretize=1
lut.EnableOpacityMapping=0
lut.HSVWrap=0
#lut.IndexedLookup=0
lut.LockScalarRange=1
lut.NanColor=[0.4980392156862745, 0.0, 0.0]
lut.NumberOfTableValues=256
lut.RGBPoints=[0.45012834668159485, 0.041672388799877925, 0.0, 0.0, 0.4562046594823599, 0.20833142595559626, 0.0, 0.0, 0.4622809722831249, 0.37500572213321126, 0.0, 0.0, 0.46835728508388996, 0.5416647592889295, 0.0, 0.0, 0.47443364573566615, 0.7083390554665446, 0.0, 0.0, 0.4805099585364312, 0.8541390096894789, 0.0, 0.0, 0.48658627133719623, 0.9374837872892348, 0.03906309605554284, 0.0, 0.49266258413796127, 1.0, 0.20833142595559626, 0.0, 0.4987388969387263, 1.0, 0.37500572213321126, 0.0, 0.5048152097394913, 1.0, 0.5416647592889295, 0.0, 0.5108915225402564, 1.0, 0.7083390554665446, 0.0, 0.5169678353410214, 1.0, 0.858808270389868, 0.03125047684443427, 0.5230441959927976, 1.0, 0.9473868925001907, 0.15625238422217136, 0.5291205087935626, 1.0, 1.0, 0.3125047684443427, 0.5351968215943277, 1.0, 1.0, 0.5624933241779202, 0.5412731343950927, 1.0, 1.0, 0.8124971389333944, 0.5458303689956665, 1.0, 1.0, 1.0]
#lut.ScalarOpacityFunction=<paraview.servermanager.PiecewiseFunction object at 0x7beeed0>
lut.ScalarRangeInitialized=1.0
lut.UseLogScale=0
lut.VectorComponent=0
lut.VectorMode='Magnitude'

# rep B
rep.CubeAxesVisibility=0
#rep.ForceUseCache=0
#rep.ForcedCacheKey=0.0
#rep.Input=<paraview.servermanager.SQImageGhosts object at 0x7bee7d0>
rep.Representation='Surface LIC'
#rep.RepresentationTypesInfo=['3D Glyphs', 'Outline', 'Points', 'Slice', 'Surface', 'Surface LIC', 'Surface With Edges', 'Volume', 'Wireframe']
rep.SelectionCellFieldDataArrayName='vtkOriginalCellIds'
rep.SelectionPointFieldDataArrayName='B'
rep.SelectionVisibility=1
rep.Visibility=1
rep.AllowSpecularHighlightingWithScalarColoring=0
rep.Ambient=0.0
rep.AmbientColor=[1.0, 1.0, 1.0]
rep.AntiAlias=0
rep.AxesOrigin=[0.0, 0.0, 0.0]
rep.BackfaceAmbientColor=[1.0, 1.0, 1.0]
rep.BackfaceDiffuseColor=[1.0, 1.0, 1.0]
rep.BackfaceOpacity=1.0
rep.BackfaceRepresentation='Follow Frontface'
rep.BlockColor={}
rep.BlockOpacity={}
rep.BlockVisibility=[]
rep.ColorArrayName=('POINT_DATA', 'mag-B')
rep.ColorAttributeType='POINT_DATA'
rep.ColorMode='Multiply'
rep.CompositeStrategy='INPLACE'
rep.CubeAxesColor=[1.0, 1.0, 1.0]
rep.CubeAxesCornerOffset=0.0
rep.CubeAxesFlyMode='Closest Triad'
rep.CubeAxesGridLineLocation='All Faces'
rep.CubeAxesInertia=1
rep.CubeAxesTickLocation='Inside'
rep.CubeAxesUseDefaultXTitle=1
rep.CubeAxesUseDefaultYTitle=1
rep.CubeAxesUseDefaultZTitle=1
rep.CubeAxesXAxisMinorTickVisibility=1
rep.CubeAxesXAxisTickVisibility=1
rep.CubeAxesXAxisVisibility=1
rep.CubeAxesXGridLines=0
rep.CubeAxesXLabelFormat='%-#6.3g'
rep.CubeAxesXTitle='X-Axis'
rep.CubeAxesYAxisMinorTickVisibility=1
rep.CubeAxesYAxisTickVisibility=1
rep.CubeAxesYAxisVisibility=1
rep.CubeAxesYGridLines=0
rep.CubeAxesYLabelFormat='%-#6.3g'
rep.CubeAxesYTitle='Y-Axis'
rep.CubeAxesZAxisMinorTickVisibility=1
rep.CubeAxesZAxisTickVisibility=1
rep.CubeAxesZAxisVisibility=1
rep.CubeAxesZGridLines=0
rep.CubeAxesZLabelFormat='%-#6.3g'
rep.CubeAxesZTitle='Z-Axis'
rep.CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
rep.CustomBoundsActive=[0, 0, 0]
rep.CustomRange=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
rep.CustomRangeActive=[0, 0, 0]
#rep.DataBounds=[2.121995791e-314, 6.02091597e-316, 8.487983164e-314, 6.02091676e-316, 8.487983164e-314, 2.0]
rep.Diffuse=1.0
rep.DiffuseColor=[1.0, 1.0, 1.0]
rep.EdgeColor=[0.0, 0.0, 0.5000076295109483]
rep.EnhanceContrast='Off'
rep.EnhancedLIC=1
rep.GenerateNoiseTexture=1
rep.HighColorContrastEnhancementFactor=0.0
rep.HighLICContrastEnhancementFactor=0.0
rep.ImpulseNoiseBackgroundValue=0.0
rep.ImpulseNoiseProbability=0.5
rep.InterpolateScalarsBeforeMapping=1
rep.Interpolation='Gouraud'
rep.InterpolationType='Cubic'
rep.LICIntensity=0.8
rep.LineWidth=1.0
rep.LookupTable=lut
rep.LowColorContrastEnhancementFactor=0.0
rep.LowLICContrastEnhancementFactor=0.1
rep.MapModeBias=0.25
rep.MapScalars=1
rep.MaskColor=[0.5, 0.5, 0.5]
rep.MaskIntensity=0.0
rep.MaskOnSurface=1
rep.MaskThreshold=0.0
rep.Masking=0
rep.MaxNoiseValue=0.8
rep.MeshVisibility=0
rep.MinNoiseValue=0.0
rep.NoiseGeneratorSeed=1
rep.NoiseGrainSize=4
rep.NoiseTextureSize=256
rep.NoiseType='Perlin'
rep.NonlinearSubdivisionLevel=1
rep.NormalizeVectors=1
rep.NumberOfNoiseLevels=1024
rep.NumberOfSteps=800
rep.Opacity=1.0
rep.Orient=0
rep.Orientation=[0.0, 0.0, 0.0]
rep.OrientationMode='Direction'
rep.Origin=[0.0, 0.0, 0.0]
rep.OriginalBoundsRangeActive=[0, 0, 0]
rep.Pickable=1
rep.PointSize=2.0
rep.Position=[0.0, 0.0, 0.0]
#rep.ScalarOpacityFunction=<paraview.servermanager.PiecewiseFunction object at 0x7bd0bd0>
rep.ScalarOpacityUnitDistance=36.871094301744
rep.Scale=[1.0, 1.0, 1.0]
rep.ScaleFactor=1636.7
rep.ScaleMode='No Data Scaling Off'
rep.Scaling=0
rep.SelectInputVectors=['POINTS', 'B']
rep.SelectMaskArray=''
rep.SelectOrientationVectors=''
rep.SelectScaleArray=''
rep.SelectionCellLabelBold=0
rep.SelectionCellLabelColor=[0.0, 1.0, 0.0]
rep.SelectionCellLabelFontFamily='Arial'
rep.SelectionCellLabelFontSize=18
rep.SelectionCellLabelFormat=''
rep.SelectionCellLabelItalic=0
rep.SelectionCellLabelJustification='Left'
rep.SelectionCellLabelOpacity=1.0
rep.SelectionCellLabelShadow=0
rep.SelectionCellLabelVisibility=0
rep.SelectionColor=[1.0, 0.0, 1.0]
rep.SelectionLineWidth=2.0
rep.SelectionOpacity=1.0
rep.SelectionPointLabelBold=0
rep.SelectionPointLabelColor=[0.5, 0.5, 0.5]
rep.SelectionPointLabelFontFamily='Arial'
rep.SelectionPointLabelFontSize=18
rep.SelectionPointLabelFormat=''
rep.SelectionPointLabelItalic=0
rep.SelectionPointLabelJustification='Left'
rep.SelectionPointLabelOpacity=1.0
rep.SelectionPointLabelShadow=0
rep.SelectionPointLabelVisibility=0
rep.SelectionPointSize=5.0
rep.SelectionRepresentation='Wireframe'
rep.SelectionUseOutline=0
rep.Shade=0
rep.Slice=0
rep.SliceMode='XY Plane'
#rep.Source=None
rep.Specular=0.1
rep.SpecularColor=[1.0, 1.0, 1.0]
rep.SpecularPower=100.0
rep.StaticMode=0
rep.StepSize=0.01
rep.SuppressLOD=0
#rep.Texture=None
rep.UseAxesOrigin=0
rep.UseLICForLOD=0
#rep.UserTransform=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
rep.VolumeRenderingMode='Smart'
#rep.WriteLog=''

Render()
WriteImage(outputImage)
rep.WriteLog = logfile
