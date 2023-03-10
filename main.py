from math import dist


def get_points(arr: list):
    def remove_every_third(arrr: list):
        return [arrr[i] for i in range(len(arrr)) if (i + 1) % 3 != 0]

    def make_points(arrr: list):
        return [(arrr[i], arrr[i + 1]) for i in range(0, len(arrr), 2)]

    values = remove_every_third(arr)
    points = make_points(values)

    return points


def get_distances(points: list):
    distances = []
    # אגודל
    distances.append(dist(points[0], points[1]))
    distances.append(dist(points[2], points[1]))
    distances.append(dist(points[2], points[3]))
    distances.append(dist(points[4], points[3]))
    # אצבע
    distances.append(dist(points[0], points[5]))
    distances.append(dist(points[6], points[5]))
    distances.append(dist(points[6], points[7]))
    distances.append(dist(points[8], points[7]))
    #  אמה
    distances.append(dist(points[0], points[9]))
    distances.append(dist(points[10], points[9]))
    distances.append(dist(points[10], points[11]))
    distances.append(dist(points[12], points[11]))
    #  קמיצה
    distances.append(dist(points[0], points[13]))
    distances.append(dist(points[14], points[13]))
    distances.append(dist(points[14], points[15]))
    distances.append(dist(points[16], points[15]))
    # זרת
    distances.append(dist(points[0], points[17]))
    distances.append(dist(points[18], points[17]))
    distances.append(dist(points[18], points[19]))
    distances.append(dist(points[20], points[19]))
    #  מרחקים בין אצבעות
    distances.append(dist(points[4], points[8]))
    distances.append(dist(points[4], points[12]))
    distances.append(dist(points[4], points[16]))
    distances.append(dist(points[4], points[20]))
    distances.append(dist(points[8], points[12]))
    distances.append(dist(points[8], points[16]))
    distances.append(dist(points[8], points[20]))
    distances.append(dist(points[12], points[16]))
    distances.append(dist(points[12], points[20]))
    distances.append(dist(points[16], points[20]))

    return distances, dist(points[0], points[5])


def get_features(distances: list, normal: float):
    features = []
    for distance in distances:
        features.append(round((distance / normal) * 100))
    return features


def process(arr: list):
    points = get_points(arr)
    distances, normal = get_distances(points)
    features = get_features(distances, normal)
    return features


class DistAlgo:
    def __init__(self):
        self.gestures = dict()

    def add_gesture(self, arr: list, name: str):
        self.gestures[name] = process(arr)

    def predict(self, arr: list):
        sign = process(arr)

        res_name, res_sign = min(self.gestures.items(), key=lambda x: dist(sign, x[1]))
        return res_name


one1 = [430.0, 321.0, 4.3989594e-09, 444.0, 280.0, 0.054327678, 439.0, 240.0, 0.06509085, 416.0, 215.0, 0.06837675,
        395.0, 209.0, 0.069847725, 437.0, 215.0, -0.0067482595, 426.0, 161.0, -0.004556157, 418.0, 127.0, -0.0014865751,
        412.0, 102.0, -0.0010925038, 415.0, 217.0, -0.033593893, 382.0, 201.0, -0.011140068, 383.0, 221.0, 0.016172433,
        393.0, 232.0, 0.028331883, 390.0, 229.0, -0.052633308, 364.0, 217.0, -0.0199762, 368.0, 235.0, 0.011336442,
        379.0, 247.0, 0.020796468, 366.0, 245.0, -0.06959919, 345.0, 224.0, -0.04467919, 343.0, 230.0, -0.022444079,
        346.0, 236.0, -0.012307464]
one2 = [444.0, 325.0, 7.489213e-09, 463.0, 283.0, 0.052461322, 459.0, 242.0, 0.060468998, 437.0, 214.0, 0.061005622,
        413.0, 207.0, 0.059841786, 459.0, 212.0, -0.010506591, 447.0, 157.0, -0.009876105, 436.0, 122.0, -0.00772985,
        430.0, 98.0, -0.007927864, 436.0, 212.0, -0.03779565, 400.0, 195.0, -0.019065378, 399.0, 216.0, 0.008201568,
        409.0, 228.0, 0.021136925, 411.0, 224.0, -0.057037983, 383.0, 218.0, -0.023544274, 386.0, 236.0, 0.008528373,
        397.0, 247.0, 0.01806261, 386.0, 240.0, -0.07485181, 371.0, 234.0, -0.04187871, 375.0, 250.0, -0.016019968,
        382.0, 261.0, -0.0047197556]
one3 = [441.0, 322.0, 6.4253505e-09, 462.0, 282.0, 0.06739865, 459.0, 243.0, 0.08454341, 441.0, 216.0, 0.09216916,
        422.0, 210.0, 0.09759196, 457.0, 212.0, 0.008946551, 446.0, 158.0, 0.01858128, 435.0, 125.0, 0.025918188, 428.0,
        102.0, 0.028769083, 435.0, 210.0, -0.021822957, 401.0, 197.0, 0.008263839, 400.0, 219.0, 0.039333228, 409.0,
        232.0, 0.053651273, 409.0, 220.0, -0.04330195, 384.0, 215.0, -0.00051650463, 387.0, 234.0, 0.033468578, 397.0,
        247.0, 0.04305684, 384.0, 235.0, -0.061991323, 368.0, 226.0, -0.025164869, 370.0, 240.0, 0.0015491117, 376.0,
        251.0, 0.013514736]

two1 = [456.0, 330.0, 7.779872e-09, 471.0, 278.0, 0.0643034, 457.0, 233.0, 0.08025674, 423.0, 211.0, 0.08722179, 394.0,
        206.0, 0.096951276, 459.0, 205.0, 0.014420783, 449.0, 148.0, 0.014495394, 442.0, 113.0, 0.01758359, 438.0, 87.0,
        0.019265207, 435.0, 212.0, -0.014327579, 407.0, 153.0, -0.0131809935, 389.0, 121.0, -0.0017591242, 376.0, 98.0,
        0.0044417004, 411.0, 227.0, -0.033792637, 377.0, 197.0, -0.007838607, 378.0, 210.0, 0.030760314, 384.0, 223.0,
        0.052868146, 387.0, 248.0, -0.05197478, 366.0, 223.0, -0.019789811, 370.0, 232.0, 0.012274491, 380.0, 243.0,
        0.033135783]
two2 = [458.0, 332.0, 6.7801667e-09, 466.0, 278.0, 0.05092453, 451.0, 232.0, 0.054974776, 420.0, 208.0, 0.050255008,
        395.0, 203.0, 0.047546428, 450.0, 210.0, -0.012056885, 435.0, 154.0, -0.027347594, 425.0, 118.0, -0.033151817,
        418.0, 92.0, -0.036998075, 433.0, 222.0, -0.04403927, 397.0, 165.0, -0.061830852, 374.0, 133.0, -0.05796692,
        356.0, 109.0, -0.055505693, 413.0, 242.0, -0.067635685, 372.0, 207.0, -0.062144514, 366.0, 215.0, -0.02632371,
        368.0, 226.0, -0.0040302747, 392.0, 267.0, -0.09095603, 361.0, 237.0, -0.07656281, 351.0, 236.0, -0.048896194,
        347.0, 239.0, -0.030045995]
two3 = [467.0, 330.0, 7.85174e-09, 476.0, 275.0, 0.06969358, 460.0, 231.0, 0.08393314, 428.0, 209.0, 0.08722583, 401.0,
        204.0, 0.09321855, 462.0, 205.0, 0.013615773, 445.0, 148.0, 0.00850888, 436.0, 113.0, 0.0074296016, 430.0, 86.0,
        0.0064277695, 440.0, 212.0, -0.020800577, 404.0, 155.0, -0.024779467, 383.0, 125.0, -0.016524259, 368.0, 101.0,
        -0.012680841, 417.0, 227.0, -0.045319, 374.0, 206.0, -0.019869773, 376.0, 224.0, 0.021169884, 385.0, 238.0,
        0.043863576, 394.0, 249.0, -0.06885096, 363.0, 233.0, -0.034715712, 365.0, 245.0, -0.0002448547, 374.0, 257.0,
        0.02150864]

three1 = [492.0, 333.0, 1.3711593e-08, 497.0, 284.0, 0.067655206, 480.0, 245.0, 0.07746663, 449.0, 227.0, 0.07780319,
          420.0, 220.0, 0.07790461, 491.0, 223.0, -0.011324012, 482.0, 166.0, -0.026112825, 475.0, 132.0, -0.027294312,
          469.0, 108.0, -0.028929481, 475.0, 231.0, -0.051254593, 461.0, 162.0, -0.0728635, 451.0, 119.0, -0.07090601,
          444.0, 84.0, -0.070283964, 454.0, 246.0, -0.08047609, 420.0, 188.0, -0.089753926, 402.0, 165.0, -0.0741064,
          390.0, 149.0, -0.0640754, 429.0, 268.0, -0.104058646, 411.0, 228.0, -0.10228192, 409.0, 220.0, -0.08598519,
          408.0, 220.0, -0.075580746]
three2 = [489.0, 330.0, 1.5558768e-08, 496.0, 284.0, 0.058578104, 481.0, 239.0, 0.069115706, 446.0, 221.0, 0.07215878,
          410.0, 218.0, 0.07704637, 496.0, 220.0, -0.0009795045, 489.0, 165.0, -0.0091675855, 486.0, 132.0,
          -0.008022186, 483.0, 107.0, -0.008204839, 476.0, 226.0, -0.032089673, 466.0, 160.0, -0.04116018, 461.0, 117.0,
          -0.035736606, 454.0, 82.0, -0.034825522, 452.0, 238.0, -0.05449258, 422.0, 184.0, -0.05181675, 409.0, 163.0,
          -0.03460241, 400.0, 147.0, -0.025575774, 425.0, 257.0, -0.07292913, 412.0, 222.0, -0.05895468, 419.0, 223.0,
          -0.03860214, 424.0, 228.0, -0.027085105]
three3 = [490.0, 331.0, 1.3897637e-08, 497.0, 282.0, 0.058917407, 481.0, 241.0, 0.06448938, 446.0, 223.0, 0.062664226,
          412.0, 220.0, 0.06134176, 493.0, 221.0, -0.022752808, 485.0, 165.0, -0.040239744, 479.0, 131.0, -0.04372149,
          474.0, 106.0, -0.046775106, 475.0, 229.0, -0.057593603, 462.0, 161.0, -0.07989916, 453.0, 117.0, -0.07999438,
          444.0, 83.0, -0.081662744, 452.0, 244.0, -0.0819199, 420.0, 188.0, -0.09012623, 404.0, 167.0, -0.076345414,
          393.0, 152.0, -0.068526246, 427.0, 265.0, -0.10140137, 412.0, 228.0, -0.09730487, 413.0, 222.0, -0.08165788,
          414.0, 223.0, -0.07272061]

four1 = [482.0, 319.0, 3.3954082e-09, 493.0, 269.0, 0.05753769, 487.0, 223.0, 0.06703174, 468.0, 192.0, 0.0676299,
         454.0, 174.0, 0.06461235, 488.0, 210.0, -0.022291206, 482.0, 152.0, -0.042513836, 477.0, 115.0, -0.044645447,
         473.0, 88.0, -0.045848742, 468.0, 217.0, -0.062653504, 455.0, 148.0, -0.09219299, 443.0, 107.0, -0.09377318,
         434.0, 75.0, -0.09322868, 445.0, 229.0, -0.0942305, 432.0, 164.0, -0.119952075, 420.0, 124.0, -0.1172082,
         412.0, 92.0, -0.11275012, 421.0, 246.0, -0.11972295, 407.0, 194.0, -0.14050339, 399.0, 161.0, -0.14177482,
         392.0, 131.0, -0.14163636]
four2 = [483.0, 322.0, 3.1287573e-09, 495.0, 275.0, 0.053093042, 490.0, 228.0, 0.06164551, 474.0, 197.0, 0.061947126,
         460.0, 179.0, 0.05904384, 491.0, 211.0, -0.020522911, 483.0, 154.0, -0.038798407, 477.0, 117.0, -0.040406153,
         472.0, 91.0, -0.04155067, 471.0, 217.0, -0.05827186, 457.0, 149.0, -0.084803775, 446.0, 108.0, -0.08657176,
         436.0, 74.0, -0.08680477, 449.0, 229.0, -0.08771699, 435.0, 164.0, -0.11048887, 423.0, 125.0, -0.107575566,
         415.0, 94.0, -0.10379423, 425.0, 246.0, -0.11165069, 411.0, 195.0, -0.13045265, 402.0, 162.0, -0.13128263,
         395.0, 133.0, -0.13110617]
four3 = [485.0, 318.0, 2.797848e-09, 497.0, 270.0, 0.053140428, 491.0, 224.0, 0.05875803, 470.0, 194.0, 0.05633303,
         452.0, 175.0, 0.050218448, 494.0, 213.0, -0.031625662, 484.0, 152.0, -0.05410447, 479.0, 116.0, -0.0565601,
         474.0, 89.0, -0.057658017, 475.0, 220.0, -0.07044396, 458.0, 148.0, -0.10128264, 446.0, 108.0, -0.10171498,
         437.0, 76.0, -0.10023664, 453.0, 232.0, -0.10050978, 437.0, 164.0, -0.12663536, 425.0, 124.0, -0.122150816,
         418.0, 93.0, -0.11657834, 428.0, 249.0, -0.124797985, 414.0, 197.0, -0.14522576, 405.0, 163.0, -0.1451601,
         399.0, 133.0, -0.14416751]

five1 = [436.0, 319.0, 8.0478575e-09, 470.0, 287.0, -0.008601187, 495.0, 243.0, -0.0270141, 516.0, 209.0, -0.047985215,
         538.0, 189.0, -0.07222483, 448.0, 196.0, -0.045865964, 445.0, 137.0, -0.07318011, 442.0, 102.0, -0.08898191,
         439.0, 74.0, -0.100776434, 420.0, 198.0, -0.062370814, 408.0, 132.0, -0.08915982, 401.0, 94.0, -0.10556869,
         393.0, 63.0, -0.11892856, 396.0, 210.0, -0.07859216, 383.0, 150.0, -0.1042375, 376.0, 112.0, -0.12181385,
         371.0, 80.0, -0.13394159, 375.0, 230.0, -0.09559331, 357.0, 186.0, -0.11824268, 347.0, 156.0, -0.13177806,
         337.0, 129.0, -0.14221257]
five2 = [443.0, 322.0, 7.553035e-09, 473.0, 285.0, 0.01611947, 495.0, 241.0, 0.0052086683, 514.0, 208.0, -0.0119516235,
         535.0, 187.0, -0.032835446, 450.0, 199.0, -0.03435541, 445.0, 139.0, -0.059561655, 442.0, 104.0, -0.07223092,
         439.0, 75.0, -0.081781805, 424.0, 204.0, -0.06209828, 410.0, 135.0, -0.08949791, 401.0, 95.0, -0.10175724,
         393.0, 63.0, -0.11128633, 399.0, 217.0, -0.08680931, 384.0, 154.0, -0.11078636, 376.0, 114.0, -0.12108698,
         371.0, 82.0, -0.12795447, 377.0, 238.0, -0.11011528, 359.0, 190.0, -0.13116494, 349.0, 157.0, -0.1400123,
         340.0, 127.0, -0.14684688]
five3 = [447.0, 320.0, 6.39525e-09, 475.0, 285.0, 0.0077995155, 497.0, 240.0, -0.005572668, 516.0, 208.0, -0.025721887,
         538.0, 188.0, -0.050112337, 449.0, 194.0, -0.030808175, 448.0, 139.0, -0.060081102, 446.0, 106.0, -0.07888719,
         443.0, 78.0, -0.09319009, 422.0, 198.0, -0.058802478, 412.0, 135.0, -0.08997074, 405.0, 97.0, -0.1106786,
         398.0, 65.0, -0.12699907, 398.0, 213.0, -0.08584645, 385.0, 155.0, -0.114484385, 379.0, 118.0, -0.13300614,
         375.0, 87.0, -0.14605059, 378.0, 236.0, -0.11259764, 361.0, 192.0, -0.13882484, 353.0, 160.0, -0.15360777,
         346.0, 130.0, -0.16504869]

like1 = [495.0, 377.0, -3.2915681e-09, 484.0, 326.0, 0.030966857, 462.0, 272.0, 0.027542459, 450.0, 227.0, 0.018586202,
         455.0, 189.0, 0.013386338, 423.0, 265.0, -0.012388813, 366.0, 275.0, 0.0036922276, 378.0, 292.0, 0.028045079,
         396.0, 296.0, 0.039595827, 416.0, 293.0, -0.037004746, 359.0, 304.0, -0.023757733, 374.0, 318.0, 0.0006109517,
         394.0, 319.0, 0.013008002, 410.0, 325.0, -0.054864787, 360.0, 332.0, -0.038218115, 376.0, 343.0, -0.012338897,
         397.0, 343.0, -0.00072171044, 408.0, 356.0, -0.070105374, 369.0, 358.0, -0.054638542, 383.0, 365.0,
         -0.03361683, 401.0, 365.0, -0.022189634]
like2 = [494.0, 374.0, -3.5555419e-09, 484.0, 323.0, 0.031313404, 463.0, 270.0, 0.027206501, 452.0, 226.0, 0.017370902,
         458.0, 188.0, 0.0113790445, 426.0, 262.0, -0.013773476, 369.0, 270.0, 0.0014719698, 379.0, 289.0, 0.025559071,
         396.0, 293.0, 0.037245963, 418.0, 289.0, -0.038552836, 362.0, 300.0, -0.026464578, 375.0, 315.0, -0.002100858,
         395.0, 318.0, 0.010856066, 412.0, 321.0, -0.056401417, 363.0, 329.0, -0.039886832, 378.0, 341.0, -0.013241614,
         398.0, 342.0, -0.00072132004, 408.0, 351.0, -0.07169154, 370.0, 354.0, -0.055354796, 384.0, 361.0,
         -0.033671748, 401.0, 361.0, -0.021625437]
like3 = [494.0, 373.0, -4.5150768e-09, 484.0, 323.0, 0.031948075, 463.0, 270.0, 0.027841879, 452.0, 225.0, 0.018190175,
         458.0, 188.0, 0.012289233, 427.0, 261.0, -0.015612462, 369.0, 270.0, -0.0020051722, 379.0, 288.0, 0.021307169,
         396.0, 293.0, 0.032653105, 419.0, 288.0, -0.040926963, 363.0, 301.0, -0.030245448, 377.0, 316.0, -0.0058717295,
         397.0, 318.0, 0.007133358, 414.0, 319.0, -0.05925513, 364.0, 329.0, -0.044014312, 380.0, 341.0, -0.016850887,
         401.0, 341.0, -0.003999982, 410.0, 350.0, -0.07493196, 372.0, 353.0, -0.05996065, 386.0, 360.0, -0.03817012,
         404.0, 360.0, -0.025976732]

ok1 = [496.0, 371.0, -1.3758036e-08, 462.0, 336.0, 0.0049312133, 442.0, 293.0, -0.001862979, 424.0, 259.0, -0.015626578,
       414.0, 230.0, -0.028139984, 493.0, 244.0, 0.016875364, 474.0, 205.0, 0.002199495, 447.0, 208.0, -0.0030018312,
       429.0, 220.0, -0.0068197995, 513.0, 239.0, -0.0041877804, 516.0, 182.0, -0.022484358, 509.0, 147.0, -0.041787,
       504.0, 117.0, -0.05699682, 529.0, 245.0, -0.02755372, 543.0, 194.0, -0.038099248, 544.0, 157.0, -0.04850901,
       546.0, 126.0, -0.058774587, 544.0, 260.0, -0.053107567, 562.0, 220.0, -0.06256779, 569.0, 191.0, -0.067773215,
       574.0, 164.0, -0.07324736]
ok2 = [497.0, 367.0, -1.3334251e-08, 464.0, 334.0, 0.0035993871, 445.0, 292.0, -0.004427721, 425.0, 259.0, -0.019612968,
       415.0, 230.0, -0.033764973, 493.0, 241.0, 0.018103233, 474.0, 204.0, 0.0040065534, 449.0, 206.0, -0.0014689316,
       432.0, 218.0, -0.0055574267, 514.0, 236.0, -0.0024510084, 515.0, 181.0, -0.019027919, 509.0, 146.0, -0.037711143,
       504.0, 117.0, -0.05257321, 530.0, 242.0, -0.025669927, 542.0, 192.0, -0.03428554, 544.0, 156.0, -0.04391503,
       545.0, 126.0, -0.05401792, 545.0, 257.0, -0.05134219, 563.0, 217.0, -0.059188843, 570.0, 189.0, -0.06357989,
       574.0, 162.0, -0.06863331]
ok3 = [498.0, 366.0, -1.2608566e-08, 464.0, 333.0, 0.0067853327, 444.0, 290.0, 0.0017189143, 425.0, 257.0, -0.011079503,
       415.0, 228.0, -0.022784155, 495.0, 241.0, 0.027244465, 476.0, 203.0, 0.017616192, 450.0, 205.0, 0.014753898,
       433.0, 217.0, 0.012187591, 515.0, 236.0, 0.0065436135, 517.0, 180.0, -0.004468458, 510.0, 146.0, -0.019934734,
       505.0, 117.0, -0.03292962, 531.0, 241.0, -0.017003229, 542.0, 191.0, -0.020672828, 544.0, 155.0, -0.027638514,
       544.0, 125.0, -0.036549322, 545.0, 255.0, -0.04304791, 562.0, 216.0, -0.047355894, 568.0, 188.0, -0.04963506,
       572.0, 163.0, -0.053388204]

algo1 = DistAlgo()
algo1.add_gesture(one2, "one2")
algo1.add_gesture(one3, "one3")
algo1.add_gesture(two2, "two2")
algo1.add_gesture(two3, "two3")
algo1.add_gesture(three2, "three2")
algo1.add_gesture(three3, "three3")
algo1.add_gesture(four2, "four2")
algo1.add_gesture(four3, "four3")
algo1.add_gesture(five2, "five2")
algo1.add_gesture(five3, "five3")
algo1.add_gesture(like2, "like2")
algo1.add_gesture(like3, "like3")
algo1.add_gesture(ok2, "ok2")
algo1.add_gesture(ok3, "ok3")

print("**********Round #1**********")
print("one1, predicted as: " + algo1.predict(one1))
print("two1, predicted as: " + algo1.predict(two1))
print("three1, predicted as: " + algo1.predict(three1))
print("four1, predicted as: " + algo1.predict(four1))
print("five1, predicted as: " + algo1.predict(five1))
print("like1, predicted as: " + algo1.predict(like1))
print("ok1, predicted as: " + algo1.predict(ok1))


algo2 = DistAlgo()
algo2.add_gesture(one1, "one1")
algo2.add_gesture(one3, "one3")
algo2.add_gesture(two1, "two1")
algo2.add_gesture(two3, "two3")
algo2.add_gesture(three1, "three1")
algo2.add_gesture(three3, "three3")
algo2.add_gesture(four1, "four1")
algo2.add_gesture(four3, "four3")
algo2.add_gesture(five1, "five1")
algo2.add_gesture(five3, "five3")
algo2.add_gesture(like1, "like1")
algo2.add_gesture(like3, "like3")
algo2.add_gesture(ok1, "ok1")
algo2.add_gesture(ok3, "ok3")

print("")
print("**********Round #2**********")
print("one2, predicted as: " + algo2.predict(one2))
print("two2, predicted as: " + algo2.predict(two2))
print("three2, predicted as: " + algo2.predict(three2))
print("four2, predicted as: " + algo2.predict(four2))
print("five2, predicted as: " + algo2.predict(five2))
print("like2, predicted as: " + algo2.predict(like2))
print("ok2, predicted as: " + algo2.predict(ok2))


algo3 = DistAlgo()
algo3.add_gesture(one1, "one1")
algo3.add_gesture(one2, "one2")
algo3.add_gesture(two1, "two1")
algo3.add_gesture(two2, "two2")
algo3.add_gesture(three1, "three1")
algo3.add_gesture(three2, "three2")
algo3.add_gesture(four1, "four1")
algo3.add_gesture(four2, "four2")
algo3.add_gesture(five1, "five1")
algo3.add_gesture(five2, "five2")
algo3.add_gesture(like1, "like1")
algo3.add_gesture(like2, "like2")
algo3.add_gesture(ok1, "ok1")
algo3.add_gesture(ok2, "ok2")

print("")
print("**********Round #3**********")
print("one3, predicted as: " + algo3.predict(one3))
print("two3, predicted as: " + algo3.predict(two3))
print("three3, predicted as: " + algo3.predict(three3))
print("four3, predicted as: " + algo3.predict(four3))
print("five3, predicted as: " + algo3.predict(five3))
print("like3, predicted as: " + algo3.predict(like3))
print("ok3, predicted as: " + algo3.predict(ok3))
