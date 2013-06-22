from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

import os

pvPrefix = '/usr/common/graphics/ParaView/builds/next/lib'
dataPrefix = '/scratch1/scratchdirs/loring/striped/pr1/'

batch=1 # commnad line run
pvpy=1  # pvpython or pvbatch
rc=1

#'INPLACE'
#'INPLACE DISJOINT'
composite=os.environ['PV_COMPOSITE_STRATEGY']
logfile=os.environ['PV_LOGFILE']
outputImage='pr1-lic-b.0.png'

if batch:
  if pvpy:
    if rc:
      ReverseConnect(os.environ['PV_PORT'])
    else:
      Connect('localhost',11111)

  LICPlugin = '%s/libSurfaceLIC.so'%(pvPrefix)
  LoadPlugin(LICPlugin, False, globals())
  LoadPlugin(LICPlugin, True, globals())

  SQPlugin = '%s/libSciberQuestToolKit.so'%(pvPrefix)
  LoadPlugin(SQPlugin, False, globals())
  LoadPlugin(SQPlugin, True, globals())

# reader
inputData='%s/pr1.bov'%(dataPrefix)
r = SQBOVReader(FileName=inputData)
r.CollectBufferSize=' 512 MB'
r.FileName='/scratch1/scratchdirs/loring/striped/pr1/pr1.bov'
r.ISubset=[0, 1023]
r.JSubset=[0, 1023]
r.KSubset=[0, 1023]
#r.ISubsetInfo=[0, 1023]
#r.JSubsetInfo=[0, 1023]
#r.KSubsetInfo=[0, 1023]
r.NumberOfIONodes=0
#r.PointArrayInfo=['b', '1', 'bx', '0', 'by', '0', 'bz', '0', 'v', '0', 'vx', '0', 'vy', '0', 'vz', '0']
r.Arrays=['b']
r.SieveBufferSize='default'
#r.TimestepValues=0.0
r.UseCollectiveIO='enabled'
r.UseDataSieving='disabled'
r.UseDeferredOpen='automatic'
r.UseDirectIO='disabled'
r.VectorProjection='None'

asc = GetAnimationScene()
asc.AnimationTime = 0.0

# view
view = GetRenderView()
view.AlphaBitPlanes=1
view.BackLightAzimuth=110.0
view.BackLightElevation=0.0
view.BackLightKBRatio=3.5
view.BackLightWarmth=0.5
view.Background=[0.31999694819562063, 0.3400015259021897, 0.4299992370489052]
view.Background2=[0.0, 0.0, 0.164705882352941]
#view.BackgroundTexture=None
#view.CacheKey=0.0
#view.Camera2DManipulators=[<paraview.servermanager.TrackballPan1 object at 0x873de90>, <paraview.servermanager.TrackballRoll object at 0x873dfd0>, <paraview.servermanager.TrackballZoom object at 0x873df10>, <paraview.servermanager.TrackballZoom object at 0x873de10>, <paraview.servermanager.TrackballZoom object at 0x873dc50>, <paraview.servermanager.TrackballZoom object at 0x873db50>, <paraview.servermanager.TrackballRoll object at 0x873dbd0>, <paraview.servermanager.TrackballPan1 object at 0x873df90>, <paraview.servermanager.TrackballRotate object at 0x89525d0>]
#view.Camera3DManipulators=[<paraview.servermanager.TrackballRotate object at 0x873de10>, <paraview.servermanager.TrackballPan1 object at 0x873dbd0>, <paraview.servermanager.TrackballZoom object at 0x873df90>, <paraview.servermanager.TrackballRoll object at 0x873dfd0>, <paraview.servermanager.TrackballRotate object at 0x873df10>, <paraview.servermanager.TrackballPan1 object at 0x873de50>, <paraview.servermanager.TrackballZoom object at 0x873dc50>, <paraview.servermanager.TrackballRotate object at 0x873db50>, <paraview.servermanager.TrackballZoom object at 0x89522d0>]
view.CenterAxesVisibility=0
view.CenterOfRotation=[511.5, 511.5, 511.5]
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
view.InteractionMode='3D'
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
#view.Representations=[<paraview.servermanager.UniformGridRepresentation object at 0x8747fd0>, <paraview.servermanager.GeometryRepresentation object at 0x873de50>]
#view.ResetCamera=Property name= ResetCamera
view.StencilCapable=1
view.StereoCapableWindow=1
view.StereoRender=0
view.StereoType='Red-Blue'
view.StillRenderImageReductionFactor=1
view.UseCache=0
view.UseGradientBackground=1
view.UseInteractiveRenderingForSceenshots=0
view.UseLight=1
view.UseOffscreenRendering=0
view.UseOffscreenRenderingForScreenshots=0
view.UseOutlineForLODRendering=1
view.UseTexturedBackground=0
view.ViewPosition=[0, 0]
view.ViewSize=[1215, 1090]
view.ViewTime=0.0
view.CameraClippingRange=[1311.3508253082925, 5305.01081316103]
#view.CameraClippingRangeInfo=[1311.3508253082925, 5305.01081316103]
view.CameraFocalPoint=[738.162231562415, 273.606281731435, 358.384763987436]
#view.CameraFocalPointInfo=[738.162231562415, 273.606281731435, 358.384763987436]
view.CameraParallelProjection=0
view.CameraParallelScale=920.533740754372
#view.CameraParallelScaleInfo=920.533740754372
view.CameraPosition=[-1580.90369530977, 1737.01194130553, 2407.1588611318]
#view.CameraPositionInfo=[-1580.90369530977, 1737.01194130553, 2407.1588611318]
view.CameraViewAngle=30.0
view.CameraViewUp=[0.24988307522374106, 0.8991156556938182, -0.3593737419498001]
#view.CameraViewUpInfo=[0.24988307522374106, 0.8991156556938182, -0.3593737419498001]
view.EyeAngle=2.0
#view.EyeTransformMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
#view.ModelTransformMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

rep = Show(r)
rep.Representation = 'Outline'
Render()

# lut
lut = GetLookupTableForArray('b',3)
lut.AllowDuplicateScalars=1
#lut.Annotations=['0.78464496 0.42983732 0.75953525', '0.78464496 0.42983732 0.75953525', '0.77841449 0.43828338 -0.47058687', '0.77841449 0.43828338 -0.47058687', '0.77575547 0.42185795 0.7130338', '0.77575547 0.42185795 0.7130338', '0.76979411 0.42794085 0.73405689', '0.76979411 0.42794085 0.73405689', '0.75533128 0.42226204 0.70997143', '0.75533128 0.42226204 0.70997143', '0.74669939 0.42856792 0.71305227', '0.74669939 0.42856792 0.71305227', '0.73873895 0.4152137 0.69847614', '0.73873895 0.4152137 0.69847614', '0.72431469 0.42126343 0.73810428', '0.72431469 0.42126343 0.73810428', '0.72212881 0.415268 0.55361229', '0.72212881 0.415268 0.55361229', '0.71092778 0.42117071 0.7229166', '0.71092778 0.42117071 0.7229166', '0.55605006 0.31290436 0.22011641', '0.55605006 0.31290436 0.22011641', '0.54886991 0.31232285 -0.3407979', '0.54886991 0.31232285 -0.3407979', '0.530155 0.35152268 0.17680722', '0.530155 0.35152268 0.17680722', '0.48235273 0.31242692 0.17265099', '0.48235273 0.31242692 0.17265099', '0.41988045 0.18947493 0.041678682', '0.41988045 0.18947493 0.041678682', '0.4192279 0.24682066 0.086142763', '0.4192279 0.24682066 0.086142763', '0.41472107 0.21807566 0.24270153', '0.41472107 0.21807566 0.24270153', '0.41419342 0.19416381 0.15247363', '0.41419342 0.19416381 0.15247363', '0.40754852 0.26661795 0.14081566', '0.40754852 0.26661795 0.14081566', '0.3540014 0.1929054 -0.20577917', '0.3540014 0.1929054 -0.20577917', '0.34639263 0.18819824 -0.22821885', '0.34639263 0.18819824 -0.22821885', '0.34353277 0.10888375 0.22360946', '0.34353277 0.10888375 0.22360946', '0.34031048 0.20273642 0.21430461', '0.34031048 0.20273642 0.21430461', '0.33641553 0.15723591 0.032152772', '0.33641553 0.15723591 0.032152772', '0.29672679 0.15890738 -0.18311453', '0.29672679 0.15890738 -0.18311453', '0.28660741 0.11023087 0.084056586', '0.28660741 0.11023087 0.084056586', '0.16003454 0.045371346 0.055603892', '0.16003454 0.045371346 0.055603892', '0.14571287 0.049083948 0.12153162', '0.14571287 0.049083948 0.12153162', '0.06458091 0.0060070902 0.048245817', '0.06458091 0.0060070902 0.048245817', '0.031679817 -0.01032684 0.10559784', '0.031679817 -0.01032684 0.10559784', '-0.015640095 -0.17361312 -0.32464963', '-0.015640095 -0.17361312 -0.32464963', '-0.018922687 -0.15633155 -0.31214941', '-0.018922687 -0.15633155 -0.31214941']
#lut.Build=Property name= Build
lut.ColorSpace='RGB'
lut.Discretize=1
lut.EnableOpacityMapping=0
lut.HSVWrap=0
lut.IndexedLookup=0
lut.LockScalarRange=1
lut.NanColor=[0.498039215686275, 0.0, 0.0]
lut.NumberOfTableValues=256
lut.RGBPoints=[0.000211422, 1.0, 1.0, 0.8, 0.006093592802916, 1.0, 0.997787441824979, 0.794583047226673, 0.011974263817254, 1.0, 0.995574883649958, 0.789166094453346, 0.01785643462017, 1.0, 0.993362325474937, 0.783764400701915, 0.023737105634508, 1.0, 0.991134508278019, 0.778347447928588, 0.029619276437424, 1.0, 0.988921950102998, 0.772930495155261, 0.035499947451762, 1.0, 0.986709391927977, 0.767513542381933, 0.041382118254678, 1.0, 0.984496833752956, 0.762111848630503, 0.047264289057594, 1.0, 0.982284275577935, 0.756694895857176, 0.053144960071932, 1.0, 0.980071717402914, 0.751277943083848, 0.059027130874848, 1.0, 0.977859159227893, 0.745860990310521, 0.064907801889186, 1.0, 0.975646601052872, 0.740459296559091, 0.070789972692102, 1.0, 0.973418783855955, 0.735042343785763, 0.07667064370644, 1.0, 0.971206225680934, 0.729625391012436, 0.082552814509356, 1.0, 0.968993667505913, 0.724208438239109, 0.088434985312272, 1.0, 0.966781109330892, 0.718806744487678, 0.09431565632661, 1.0, 0.964568551155871, 0.713389791714351, 0.100197827129526, 1.0, 0.96235599298085, 0.707972838941024, 0.106078498143864, 1.0, 0.960143434805829, 0.702555886167697, 0.11196066894678, 1.0, 0.957930876630808, 0.697154192416266, 0.117841339961118, 1.0, 0.95570305943389, 0.691737239642939, 0.123723510764034, 1.0, 0.953490501258869, 0.686320286869612, 0.12960568156695, 1.0, 0.951277943083848, 0.680903334096284, 0.135486352581288, 1.0, 0.949065384908827, 0.675486381322957, 0.141368523384204, 1.0, 0.946852826733806, 0.670084687571527, 0.147249194398542, 1.0, 0.944640268558785, 0.664667734798199, 0.153131365201458, 1.0, 0.942427710383764, 0.659250782024872, 0.159012036215796, 1.0, 0.940215152208743, 0.653833829251545, 0.164894207018712, 1.0, 0.937987335011826, 0.648432135500114, 0.17077487803305, 1.0, 0.935774776836805, 0.643015182726787, 0.176657048835966, 1.0, 0.933562218661784, 0.63759822995346, 0.182539219638882, 1.0, 0.931349660486763, 0.632181277180133, 0.18841989065322, 0.999984740978103, 0.929106584267948, 0.626810101472496, 0.194302061456136, 0.99986266880293, 0.92664988174258, 0.621637293049516, 0.200182732470474, 0.999740596627756, 0.924177920195316, 0.616464484626535, 0.20606490327339, 0.999618524452583, 0.921721217669947, 0.611306935225452, 0.211945574287728, 0.999496452277409, 0.919264515144579, 0.606134126802472, 0.217827745090644, 0.999374380102235, 0.916807812619211, 0.600976577401389, 0.22370991589356, 0.999252307927062, 0.914335851071946, 0.595803768978408, 0.229590586907898, 0.999130235751888, 0.911879148546578, 0.590630960555428, 0.235472757710814, 0.998992904554818, 0.90942244602121, 0.585473411154345, 0.241353428725152, 0.998870832379644, 0.906965743495842, 0.580300602731365, 0.247235599528068, 0.998748760204471, 0.904493781948577, 0.575127794308385, 0.253116270542406, 0.998626688029297, 0.902037079423209, 0.569970244907301, 0.258998441345322, 0.998504615854124, 0.899580376897841, 0.564797436484321, 0.264880612148238, 0.99838254367895, 0.897108415350576, 0.559624628061341, 0.270761283162576, 0.998260471503777, 0.894651712825208, 0.554467078660258, 0.276643453965492, 0.998138399328603, 0.89219501029984, 0.549294270237278, 0.28252412497983, 0.998016327153429, 0.889738307774472, 0.544121461814298, 0.288406295782746, 0.997894254978256, 0.887281605249103, 0.538963912413214, 0.294286966797084, 0.997772182803082, 0.884809643701839, 0.533791103990234, 0.3001691376, 0.997650110627909, 0.882352941176471, 0.528633554589151, 0.306051308402916, 0.997528038452735, 0.879896238651102, 0.523460746166171, 0.311931979417254, 0.997405966277562, 0.877439536125734, 0.518287937743191, 0.31781415022017, 0.997283894102388, 0.87496757457847, 0.513130388342107, 0.323694821234508, 0.997161821927214, 0.872510872053101, 0.507957579919127, 0.329576992037424, 0.997024490730144, 0.870054169527733, 0.502784771496147, 0.335457663051762, 0.996902418554971, 0.867582207980468, 0.497627222095064, 0.341339833854678, 0.996780346379797, 0.8651255054551, 0.492454413672084, 0.347222004657594, 0.996658274204623, 0.862668802929732, 0.487296864271, 0.353102675671932, 0.99653620202945, 0.860212100404364, 0.48212405584802, 0.358984846474848, 0.996414129854276, 0.857740138857099, 0.47695124742504, 0.364865517489186, 0.996292057679103, 0.855283436331731, 0.471793698023957, 0.370747688292102, 0.996169985503929, 0.852826733806363, 0.466620889600977, 0.37662835930644, 0.996078431372549, 0.849774929427024, 0.461448081177997, 0.382510530109356, 0.996078431372549, 0.844983596551461, 0.456290531776913, 0.388392700912272, 0.996078431372549, 0.840192263675898, 0.451117723353933, 0.39427337192661, 0.996078431372549, 0.835385671778439, 0.445944914930953, 0.400155542729526, 0.996078431372549, 0.830594338902876, 0.44078736552987, 0.406036213743864, 0.996078431372549, 0.825787747005417, 0.435614557106889, 0.41191838454678, 0.996078431372549, 0.820996414129854, 0.430457007705806, 0.417799055561118, 0.996078431372549, 0.816189822232395, 0.425284199282826, 0.423681226364034, 0.996078431372549, 0.811398489356832, 0.420111390859846, 0.42956339716695, 0.996078431372549, 0.806591897459373, 0.414953841458763, 0.435444068181288, 0.996078431372549, 0.80180056458381, 0.409781033035782, 0.441326238984204, 0.996078431372549, 0.796993972686351, 0.404608224612802, 0.447206909998542, 0.996078431372549, 0.792202639810788, 0.399450675211719, 0.453089080801458, 0.996078431372549, 0.787411306935225, 0.394277866788739, 0.458969751815796, 0.996078431372549, 0.782604715037766, 0.389105058365759, 0.464851922618712, 0.996078431372549, 0.777813382162203, 0.383947508964675, 0.47073259363305, 0.996078431372549, 0.773006790264744, 0.378774700541695, 0.476614764435966, 0.996078431372549, 0.768215457389181, 0.373617151140612, 0.482496935238882, 0.996078431372549, 0.763408865491722, 0.368444342717632, 0.48837760625322, 0.996078431372549, 0.758617532616159, 0.363271534294652, 0.494259777056136, 0.996078431372549, 0.7538109407187, 0.358113984893568, 0.500140448070474, 0.996078431372549, 0.749019607843137, 0.352941176470588, 0.50602261887339, 0.996078431372549, 0.744228274967575, 0.347768368047608, 0.511903289887728, 0.996078431372549, 0.739421683070115, 0.342610818646525, 0.517785460690644, 0.996078431372549, 0.734630350194553, 0.337438010223545, 0.52366763149356, 0.996078431372549, 0.729823758297093, 0.332265201800565, 0.529548302507898, 0.996078431372549, 0.72503242542153, 0.327107652399481, 0.535430473310814, 0.996078431372549, 0.720225833524071, 0.321934843976501, 0.541311144325152, 0.996078431372549, 0.715434500648508, 0.316777294575418, 0.547193315128068, 0.996078431372549, 0.710627908751049, 0.311604486152438, 0.553073986142406, 0.996078431372549, 0.705836575875486, 0.306431677729458, 0.558956156945322, 0.996078431372549, 0.701045242999924, 0.301274128328374, 0.564838327748238, 0.996032654306859, 0.696330205233844, 0.297306782635233, 0.570718998762576, 0.995910582131685, 0.691783016708629, 0.295338368810559, 0.576601169565492, 0.995788509956512, 0.687220569161517, 0.293369954985885, 0.58248184057983, 0.995666437781338, 0.682673380636301, 0.291401541161212, 0.588364011382746, 0.995544365606165, 0.678126192111086, 0.289433127336538, 0.594244682397084, 0.995422293430991, 0.67357900358587, 0.287464713511864, 0.6001268532, 0.995300221255818, 0.669016556038758, 0.28549629968719, 0.606009024002916, 0.995178149080644, 0.664469367513542, 0.283527885862516, 0.611889695017254, 0.995040817883574, 0.659922178988327, 0.281559472037842, 0.61777186582017, 0.9949187457084, 0.655359731441215, 0.279591058213169, 0.623652536834508, 0.994796673533227, 0.650812542915999, 0.277622644388495, 0.629534707637424, 0.994674601358053, 0.646265354390784, 0.275654230563821, 0.635415378651762, 0.994552529182879, 0.641702906843671, 0.273685816739147, 0.641297549454678, 0.994430457007706, 0.637155718318456, 0.271717402914473, 0.647179720257594, 0.994308384832532, 0.63260852979324, 0.269748989089799, 0.653060391271932, 0.994186312657359, 0.628046082246128, 0.267780575265125, 0.658942562074848, 0.994064240482185, 0.623498893720912, 0.265812161440452, 0.664823233089186, 0.993942168307012, 0.618951705195697, 0.263843747615778, 0.670705403892102, 0.993820096131838, 0.614389257648585, 0.261875333791104, 0.67658607490644, 0.993698023956664, 0.609842069123369, 0.25990691996643, 0.682468245709356, 0.993575951781491, 0.605294880598154, 0.257938506141756, 0.688350416512272, 0.993453879606317, 0.600732433051041, 0.255970092317082, 0.69423108752661, 0.993331807431144, 0.596185244525826, 0.254001678492409, 0.700113258329526, 0.99320973525597, 0.59163805600061, 0.252033264667735, 0.705993929343864, 0.9930724040589, 0.587075608453498, 0.250064850843061, 0.71187610014678, 0.992950331883726, 0.582528419928283, 0.248096437018387, 0.717756771161118, 0.992828259708553, 0.577981231403067, 0.246128023193713, 0.723638941964034, 0.992706187533379, 0.573418783855955, 0.244159609369039, 0.72952111276695, 0.992584115358206, 0.568871595330739, 0.242191195544366, 0.735401783781288, 0.992462043183032, 0.564324406805524, 0.240207522697795, 0.741283954584204, 0.992339971007858, 0.559761959258412, 0.238254367895018, 0.747164625598542, 0.992217898832685, 0.555214770733196, 0.236270695048447, 0.753046796401458, 0.992095826657511, 0.549065384908827, 0.2341802090486, 0.758927467415796, 0.991973754482338, 0.541313801785306, 0.231967650873579, 0.764809638218712, 0.991851682307164, 0.533562218661784, 0.229755092698558, 0.77069030923305, 0.991729610131991, 0.525810635538262, 0.227542534523537, 0.776572480035966, 0.991607537956817, 0.51805905241474, 0.225329976348516, 0.782454650838882, 0.991485465781643, 0.510307469291218, 0.223117418173495, 0.78833532185322, 0.99136339360647, 0.502555886167697, 0.220904859998474, 0.794217492656136, 0.991241321431296, 0.494804303044175, 0.218692301823453, 0.800098163670474, 0.991103990234226, 0.487052719920653, 0.216464484626535, 0.80598033447339, 0.990981918059052, 0.479301136797131, 0.214251926451514, 0.811861005487728, 0.990859845883879, 0.47154955367361, 0.212039368276493, 0.817743176290644, 0.990737773708705, 0.463813229571984, 0.209826810101472, 0.82362534709356, 0.990615701533532, 0.456061646448463, 0.207614251926452, 0.829506018107898, 0.990493629358358, 0.448310063324941, 0.205401693751431, 0.835388188910814, 0.990371557183185, 0.440558480201419, 0.20318913557641, 0.841268859925152, 0.990249485008011, 0.432806897077897, 0.200976577401389, 0.847151030728068, 0.990127412832837, 0.425055313954376, 0.198748760204471, 0.853031701742406, 0.990005340657664, 0.417303730830854, 0.19653620202945, 0.858913872545322, 0.98988326848249, 0.409552147707332, 0.194323643854429, 0.864796043348238, 0.989761196307317, 0.40180056458381, 0.192111085679408, 0.870676714362576, 0.989639124132143, 0.394048981460288, 0.189898527504387, 0.876558885165492, 0.98951705195697, 0.386297398336767, 0.187685969329366, 0.88243955617983, 0.989394979781796, 0.378545815213245, 0.185473411154345, 0.888321726982746, 0.989272907606622, 0.370794232089723, 0.183245593957427, 0.894202397997084, 0.989135576409552, 0.363042648966201, 0.181033035782406, 0.9000845688, 0.989013504234379, 0.355291065842679, 0.178820477607385, 0.905966739602916, 0.988891432059205, 0.347539482719158, 0.176607919432364, 0.911847410617254, 0.988769359884031, 0.339787899595636, 0.174395361257343, 0.91772958142017, 0.988647287708858, 0.332036316472114, 0.172182803082322, 0.923610252434508, 0.988525215533684, 0.324284733348592, 0.169970244907301, 0.929492423237424, 0.988403143358511, 0.316533150225071, 0.16775768673228, 0.935373094251762, 0.988281071183337, 0.308781567101549, 0.165529869535363, 0.941255265054678, 0.986312657358663, 0.301884489204242, 0.163622491798276, 0.947137435857594, 0.983230334935531, 0.295490959029526, 0.161913481345846, 0.953018106871932, 0.980163271534295, 0.289082169832914, 0.160189211871519, 0.958900277674848, 0.977080949111162, 0.282688639658198, 0.158464942397192, 0.964780948689186, 0.974013885709926, 0.276295109483482, 0.156740672922866, 0.970663119492102, 0.970931563286793, 0.269901579308766, 0.155016403448539, 0.97654379050644, 0.967864499885557, 0.263492790112154, 0.153292133974212, 0.982425961309356, 0.964782177462425, 0.257099259937438, 0.151567864499886, 0.988308132112272, 0.961699855039292, 0.250705729762722, 0.149843595025559, 0.99418880312661, 0.958632791638056, 0.244312199588006, 0.148134584573129, 1.00007097392953, 0.955550469214923, 0.237903410391394, 0.146410315098802, 1.00595164494386, 0.952483405813687, 0.231509880216678, 0.144686045624475, 1.01183381574678, 0.949401083390555, 0.225116350041962, 0.142961776150149, 1.01771448676112, 0.946334019989319, 0.218722819867247, 0.141237506675822, 1.02359665756403, 0.943251697566186, 0.212314030670634, 0.139513237201495, 1.02947882836695, 0.940169375143053, 0.205920500495918, 0.137788967727169, 1.03535949938129, 0.937102311741817, 0.199526970321202, 0.136064698252842, 1.0412416701842, 0.934019989318685, 0.193133440146487, 0.134340428778515, 1.04712234119854, 0.930952925917449, 0.186724650949874, 0.132631418326085, 1.05300451200146, 0.927870603494316, 0.180331120775158, 0.130907148851759, 1.0588851830158, 0.92480354009308, 0.173937590600443, 0.129182879377432, 1.06476735381871, 0.921721217669947, 0.16752880140383, 0.127458609903105, 1.07064802483305, 0.918654154268711, 0.161135271229114, 0.125734340428779, 1.07653019563597, 0.915571831845579, 0.154741741054398, 0.124010070954452, 1.08241236643888, 0.912489509422446, 0.148348210879683, 0.122285801480125, 1.08829303745322, 0.90942244602121, 0.14193942168307, 0.120561532005798, 1.09417520825614, 0.906340123598077, 0.135545891508354, 0.118852521553368, 1.10005587927047, 0.903273060196841, 0.129152361333639, 0.117128252079042, 1.10593805007339, 0.900190737773709, 0.122758831158923, 0.115403982604715, 1.11181872108773, 0.897108415350576, 0.11635004196231, 0.113679713130388, 1.11770089189064, 0.89404135194934, 0.109956511787594, 0.111955443656062, 1.12358306269356, 0.890959029526207, 0.103562981612879, 0.110231174181735, 1.1294637337079, 0.886686503395132, 0.0995651178759441, 0.110719462882429, 1.13534590451081, 0.882017242694743, 0.0963607232776379, 0.111955443656062, 1.14122657552515, 0.877332722972457, 0.0931715877012284, 0.113191424429694, 1.14710874632807, 0.872663462272068, 0.0899671931029221, 0.11441214618143, 1.15298941734241, 0.867994201571679, 0.0867627985046159, 0.115648126955062, 1.15887158814532, 0.863309681849393, 0.0835736629282063, 0.116884107728695, 1.16475375894824, 0.858640421149004, 0.0803692683299001, 0.11810482948043, 1.17063442996258, 0.853971160448615, 0.0771648737315938, 0.119340810254063, 1.17651660076549, 0.849286640726329, 0.0739757381551843, 0.120561532005798, 1.18239727177983, 0.84461738002594, 0.070771343556878, 0.121797512779431, 1.18827944258275, 0.839932860303655, 0.0675669489585718, 0.123033493553063, 1.19416011359708, 0.835263599603265, 0.0643778133821622, 0.124254215304799, 1.2000422844, 0.830594338902876, 0.061173418783856, 0.125490196078431, 1.20592445520292, 0.82590981918059, 0.0579842832074464, 0.126726176852064, 1.21180512621725, 0.821240558480201, 0.0547798886091402, 0.127946898603799, 1.21768729702017, 0.816556038757916, 0.0515754940108339, 0.129182879377432, 1.22356796803451, 0.811886778057527, 0.0483863584344244, 0.130403601129168, 1.22945013883742, 0.807217517357137, 0.0451819638361181, 0.1316395819028, 1.23533080985176, 0.802532997634852, 0.0419775692378119, 0.132875562676432, 1.24121298065468, 0.797863736934463, 0.0387884336614023, 0.134096284428168, 1.24709515145759, 0.793194476234073, 0.0355840390630961, 0.135332265201801, 1.25297582247193, 0.788509956511788, 0.0323949034866865, 0.136568245975433, 1.25885799327485, 0.783840695811398, 0.0291905088883803, 0.137788967727169, 1.26473866428919, 0.779156176089113, 0.025986114290074, 0.139024948500801, 1.2706208350921, 0.774486915388724, 0.0227969787136645, 0.140260929274434, 1.27650150610644, 0.769817654688335, 0.0195925841153582, 0.141481651026169, 1.28238367690936, 0.765133134966049, 0.016388189517052, 0.142717631799802, 1.28826584771227, 0.76046387426566, 0.0131990539406424, 0.143938353551537, 1.29414651872661, 0.755779354543374, 0.00999465934233616, 0.14517433432517, 1.30002868952953, 0.751110093842985, 0.00679026474402991, 0.146410315098802, 1.30590936054386, 0.746440833142596, 0.00360112916762036, 0.147631036850538, 1.31179153134678, 0.74175631342031, 0.000396734569314107, 0.14886701762417, 1.31767220236112, 0.734615091172656, 0.0, 0.149019607843137, 1.32355437316403, 0.727107652399481, 0.0, 0.149019607843137, 1.32943654396695, 0.719600213626307, 0.0, 0.149019607843137, 1.33531721498129, 0.712092774853132, 0.0, 0.149019607843137, 1.3411993857842, 0.704585336079957, 0.0, 0.149019607843137, 1.34708005679854, 0.697093156328679, 0.0, 0.149019607843137, 1.35296222760146, 0.689585717555505, 0.0, 0.149019607843137, 1.3588428986158, 0.68207827878233, 0.0, 0.149019607843137, 1.36472506941871, 0.674570840009155, 0.0, 0.149019607843137, 1.37060574043305, 0.667063401235981, 0.0, 0.149019607843137, 1.37648791123597, 0.659555962462806, 0.0, 0.149019607843137, 1.38237008203888, 0.652063782711528, 0.0, 0.149019607843137, 1.38825075305322, 0.644556343938354, 0.0, 0.149019607843137, 1.39413292385614, 0.637048905165179, 0.0, 0.149019607843137, 1.40001359487047, 0.629541466392004, 0.0, 0.149019607843137, 1.40589576567339, 0.62203402761883, 0.0, 0.149019607843137, 1.41177643668773, 0.614526588845655, 0.0, 0.149019607843137, 1.41765860749064, 0.607034409094377, 0.0, 0.149019607843137, 1.42354077829356, 0.599526970321202, 0.0, 0.149019607843137, 1.4294214493079, 0.592019531548028, 0.0, 0.149019607843137, 1.43530362011081, 0.584512092774853, 0.0, 0.149019607843137, 1.44118429112515, 0.577004654001678, 0.0, 0.149019607843137, 1.44706646192807, 0.569497215228504, 0.0, 0.149019607843137, 1.45294713294241, 0.562005035477226, 0.0, 0.149019607843137, 1.45882930374532, 0.554497596704051, 0.0, 0.149019607843137, 1.46471147454824, 0.546990157930877, 0.0, 0.149019607843137, 1.47059214556258, 0.539482719157702, 0.0, 0.149019607843137, 1.47647431636549, 0.531975280384527, 0.0, 0.149019607843137, 1.48235498737983, 0.524467841611353, 0.0, 0.149019607843137, 1.48823715818275, 0.516975661860075, 0.0, 0.149019607843137, 1.49411782919708, 0.5094682230869, 0.0, 0.149019607843137, 1.5, 0.501960784313725, 0.0, 0.149019607843137]
#lut.ScalarOpacityFunction=<paraview.servermanager.PiecewiseFunction object at 0x876cad0>
lut.ScalarRangeInitialized=1.0
lut.UseLogScale=0
lut.VectorComponent=0
lut.VectorMode='Magnitude'

# lic
rep.CubeAxesVisibility=0
#rep.ForceUseCache=0
#rep.ForcedCacheKey=0.0
#rep.Input=<paraview.servermanager.SQBOVReader object at 0x8747550>
rep.Representation='Surface LIC'
#rep.RepresentationTypesInfo=['3D Glyphs', 'Outline', 'Points', 'Slice', 'Surface', 'Surface LIC', 'Surface With Edges', 'Volume', 'Wireframe']
rep.SelectionCellFieldDataArrayName='vtkOriginalCellIds'
rep.SelectionPointFieldDataArrayName='b'
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
rep.ColorArrayName=('POINT_DATA', 'b')
rep.ColorAttributeType='POINT_DATA'
rep.ColorMode='Multiply'
rep.CompositeStrategy=composite
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
#rep.DataBounds=[8.4879831644e-314, 9.9118423395993e-311, -4.399029464473897e+163, 5.2239035e-316, 8.487983164e-314, 1.1407849372233e-310]
rep.Diffuse=1.0
rep.DiffuseColor=[1.0, 1.0, 1.0]
rep.EdgeColor=[0.0, 0.0, 0.5000076295109483]
rep.EnhanceContrast='LIC and Color'
rep.EnhancedLIC=1
rep.GenerateNoiseTexture=0
rep.HighColorContrastEnhancementFactor=0.0
rep.HighLICContrastEnhancementFactor=0.0
rep.ImpulseNoiseBackgroundValue=0.0
rep.ImpulseNoiseProbability=1.0
rep.InterpolateScalarsBeforeMapping=1
rep.Interpolation='Gouraud'
rep.InterpolationType='Cubic'
rep.LICIntensity=0.8
rep.LineWidth=1.0
rep.LookupTable=lut
rep.LowColorContrastEnhancementFactor=0.0
rep.LowLICContrastEnhancementFactor=0.25
rep.MapModeBias=0.23
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
rep.NumberOfSteps=500
rep.Opacity=1.0
rep.Orient=0
rep.Orientation=[0.0, 0.0, 0.0]
rep.OrientationMode='Direction'
rep.Origin=[0.0, 0.0, 0.0]
rep.OriginalBoundsRangeActive=[0, 0, 0]
rep.Pickable=1
rep.PointSize=2.0
rep.Position=[0.0, 0.0, 0.0]
#rep.ScalarOpacityFunction=<paraview.servermanager.PiecewiseFunction object at 0x873dd90>
rep.ScalarOpacityUnitDistance=1.73205080756888
rep.Scale=[1.0, 1.0, 1.0]
rep.ScaleFactor=102.3
rep.ScaleMode='No Data Scaling Off'
rep.Scaling=0
rep.SelectInputVectors=['POINTS', 'b']
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
