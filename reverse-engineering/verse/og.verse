using { /Fortnite.com/Devices }
using { /Verse.org/Native }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Verse.org/Verse}

outp := class(log_channel){}

inp := class(creative_device) {
    ### VARIABLES ###
    asciiTable : [int]string = map{
        32 => " ", 33 => "!", 34 => "\"", 35 => "#",
        36 => "$", 37 => "%", 38 => "&", 39 => "'",
        40 => "(", 41 => ")", 42 => "*", 43 => "+",
        44 => ",", 45 => "-", 46 => ".", 47 => "/",
        48 => "0", 49 => "1", 50 => "2", 51 => "3",
        52 => "4", 53 => "5", 54 => "6", 55 => "7",
        56 => "8", 57 => "9", 58 => ":", 59 => ";",
        60 => "<", 61 => "=", 62 => ">", 63 => "?",
        64 => "@", 65 => "A", 66 => "B", 67 => "C",
        68 => "D", 69 => "E", 70 => "F", 71 => "G",
        72 => "H", 73 => "I", 74 => "J", 75 => "K",
        76 => "L", 77 => "M", 78 => "N", 79 => "O",
        80 => "P", 81 => "Q", 82 => "R", 83 => "S",
        84 => "T", 85 => "U", 86 => "V", 87 => "W",
        88 => "X", 89 => "Y", 90 => "Z", 91 => "[",
        92 => "\\", 93 => "]", 94 => "^", 95 => "_",
        96 => "`", 97 => "a", 98 => "b", 99 => "c",
        100 => "d", 101 => "e", 102 => "f", 103 => "g",
        104 => "h", 105 => "i", 106 => "j", 107 => "k",
        108 => "l", 109 => "m", 110 => "n", 111 => "o",
        112 => "p", 113 => "q", 114 => "r", 115 => "s",
        116 => "t", 117 => "u", 118 => "v", 119 => "w",
        120 => "x", 121 => "y", 122 => "z", 123 => "\{",
        124 => "|"
    }

    # output
    Logger : log = log{Channel := outp}

    @editable # 480 switch devices
    InputDevices : []switch_device = array{}

    # array of 480 logics
    var InputBits : []logic = array{}

    @editable # button to check flag
    CheckFlagBtn:button_device = button_device{}

    # pairs to exchange bits
    pairs : []tuple(int,int) = array{(180, 252), (174, 213), (110, 395), (38, 364), (255, 171), (399, 301), (93, 194), (262, 105), (169, 18), (283, 433), (346, 181), (247, 151), (408, 67), (360, 333), (57, 418), (290, 322), (463, 219), (389, 467), (317, 420), (65, 116), (162, 31), (327, 449), (158, 130), (279, 226), (79, 404), (321, 442), (19, 357), (60, 127), (41, 296), (293, 319), (244, 133), (195, 387), (220, 62), (250, 77), (473, 288), (234, 134), (325, 385), (138, 266), (254, 76), (330, 201), (435, 417), (400, 86), (431, 30), (141, 304), (456, 114), (89, 106), (12, 432), (265, 248), (388, 446), (328, 356), (308, 27), (95, 119), (63, 359), (90, 44), (245, 362), (88, 368), (58, 394), (185, 375), (48, 354), (49, 179), (347, 374), (348, 157), (205, 183), (415, 100), (103, 107), (97, 33), (474, 284), (261, 369), (273, 477), (314, 320), (297, 164), (451, 3), (460, 332), (224, 47), (462, 351), (142, 115), (140, 315), (312, 246), (54, 264), (136, 338), (468, 39), (324, 339), (380, 84), (197, 379), (102, 427), (472, 200), (104, 147), (251, 278), (295, 228), (452, 358), (202, 422), (406, 361), (281, 232), (148, 267), (334, 371), (193, 0), (457, 131), (208, 225), (407, 215), (298, 176), (132, 443), (440, 258), (35, 111), (101, 37), (256, 426), (203, 274), (25, 206), (61, 231), (291, 421), (192, 428), (137, 355), (454, 241), (15, 455), (294, 350), (373, 352), (285, 187), (412, 282), (124, 99), (275, 311), (123, 28), (121, 168), (91, 188), (218, 397), (243, 398), (270, 117), (475, 211), (113, 42), (163, 17), (68, 146), (199, 112), (160, 51), (391, 377), (217, 337), (126, 403), (268, 409), (207, 74), (343, 139), (24, 378), (383, 340), (186, 466), (87, 92), (313, 410), (230, 402), (96, 453), (21, 94), (85, 154), (269, 307), (419, 260), (56, 271), (50, 214), (405, 287), (365, 376), (366, 263), (55, 204), (53, 120), (461, 471), (237, 249), (1, 233), (161, 216), (302, 437), (242, 450), (69, 7), (335, 80), (277, 396), (16, 66), (2, 318), (83, 331), (45, 36), (223, 310), (309, 78), (6, 272), (52, 173), (191, 286), (23, 178), (370, 342), (189, 4), (436, 445), (227, 329), (414, 82), (152, 384), (165, 240), (150, 81), (46, 253), (401, 413), (170, 276), (259, 363), (382, 316), (323, 175), (73, 159), (108, 109), (306, 236), (238, 13), (459, 196), (75, 305), (448, 239), (257, 425), (229, 476), (172, 210), (479, 149), (11, 29), (129, 381), (5, 326), (182, 43), (128, 167), (280, 434), (14, 424), (292, 118), (145, 212), (393, 198), (9, 300), (177, 155), (447, 441), (26, 70), (190, 289), (40, 156), (390, 144), (98, 465), (458, 372), (303, 32), (64, 135), (166, 72), (438, 478), (299, 336), (153, 464), (10, 386), (444, 341), (34, 423), (221, 439), (349, 367), (59, 469), (470, 392), (209, 184), (222, 122), (416, 344), (8, 235), (345, 71), (430, 353), (20, 125), (22, 411), (429, 143)}

    # array of 480 logics but after exchanging
    var Exchanged : []logic = array{}

    # reverse array of logics for flag comparison after exchanging
    FlagBits : []logic = array{true, false, true, true, true, true, false, false, true, false, true, false, true, false, true, true, true, false, true, false, false, false, true, true, true, true, false, true, false, true, true, true, true, false, true, false, false, true, true, false, false, false, false, false, true, false, true, true, true, true, true, false, false, false, true, false, true, true, false, false, true, true, false, false, true, true, true, false, false, true, false, false, false, true, true, true, true, true, true, true, true, false, true, true, false, true, true, true, false, false, true, false, true, true, true, false, true, false, true, false, false, false, false, true, true, false, false, true, true, false, true, false, true, true, false, false, true, true, false, true, false, true, true, false, true, false, false, false, true, true, true, true, true, false, false, false, false, true, true, true, false, false, true, false, false, true, false, true, true, true, false, true, false, false, true, false, true, true, true, true, false, true, true, false, false, false, true, false, false, false, false, false, true, false, false, false, false, true, false, true, false, false, true, true, true, true, false, true, true, true, true, true, false, true, true, true, true, false, false, true, true, false, false, true, true, true, true, true, false, true, true, true, false, true, false, true, false, true, true, false, false, false, true, true, false, true, true, false, true, false, false, true, true, false, true, true, true, true, true, true, false, false, true, false, false, false, true, true, true, true, true, false, true, true, false, false, true, true, false, false, true, false, true, true, true, true, false, true, true, true, false, true, true, true, true, true, true, true, true, false, false, true, false, true, false, true, false, false, true, true, false, true, true, true, false, true, true, false, true, false, true, true, false, true, false, false, true, true, false, true, true, true, false, false, false, true, true, true, false, true, true, true, true, false, true, false, false, false, true, true, true, true, false, true, false, true, true, false, false, false, true, true, false, true, false, true, false, true, false, false, true, true, false, false, false, false, false, false, false, false, true, false, false, true, false, false, true, true, true, true, false, false, false, true, true, false, false, false, true, true, false, false, true, true, false, true, true, true, true, false, true, false, true, false, true, true, false, false, true, true, true, true, true, false, true, true, true, true, true, true, false, true, false, false, true, true, false, false, true, true, true, true, true, false, false, false, false, false, false, false, true, true, false, true, false, false, true, true, false, false, true, false, true, true, true, false, true, true, false, false, true, false, true, false, false, true, true, false, true, true, true, true, true, true, true, false, true, false, false, true, false, true, false, false, false, true, true, true, true, true}


    ### FUNCTIONS ###
    # Print booleans
    PrintLogic(l:logic):string = {
        if (l?) {
            return "True"
        }
        else {
            return "False"
        }
    }
    
    # turns an array of switch devices (InputDevices) into an array of logics (InputBits)
    ParseInput():void = {
        # clear InputBits
        var clearArray : []logic = array{}
        for (i := 1..InputDevices.Length) {
            set clearArray += array{false}
        }
        set InputBits = clearArray
        #Logger.Print("InputBits length = {InputBits.Length}")

        # fill in InputBits
        for (Index := 0..InputDevices.Length - 1) {
            if (Element := InputDevices[Index]) {
                var s : logic = false
                if (Element.GetCurrentState[]) {
                    set s = true
                }

                if (set InputBits[Index] = s) {}
                #else {Logger.Print("Couldn't set InputBit")}
                #Logger.Print("InputDevices[{Index}] = {PrintLogic(s)}")
            }
        }
    }

    # array of logics to ascii string
    BinaryToAscii(bitArray:[]logic):string = {
        # ensure array length is divisible by 8
        if (Mod[bitArray.Length, 8] <> 0) {
            return "Error: bitArray length not divisible by 8"
        }

        var retval : string = "";
        var Chunks : int = 0;

        if (set Chunks = Floor(bitArray.Length/8)) {}
        #Logger.Print("Length = {bitArray.Length}")
        #Logger.Print("Chunks = {Chunks}")

        for (i := 0..Chunks - 1) {
            #Logger.Print("In loop")
            var decimal : int = 0
            for (j := 0..8) {
                if (bitArray[(i*8)+j]=true) {
                    if (X := Floor[Pow(2.0, (7-j)*1.0)]) {
                        #Logger.Print("X = {X}")
                        set decimal += X
                    }
                    #else {Logger.Print("Conversion failed")}
                }
                #else {Logger.Print("Bit Not True")}
            }

            if (character := asciiTable[decimal]) {
                set retval += character
            }
            else {
                set retval += "?"
            }
        }

        return retval
    }

    # exchange bits using pairs variable
    ExchangeBits():void = {
        # set Exchanged
        var clearArray : []logic = array{}
        for (i := 1..InputBits.Length) {
            set clearArray += array{false}
        }
        set Exchanged = clearArray

        # exchange bits
        for (i := 0..pairs.Length - 1) {
            if (t : tuple(int,int) = pairs[i]) {
                x : int = t(0)
                y : int = t(1)

                if (set Exchanged[x] = InputBits[y]) {}
                if (set Exchanged[y] = InputBits[x]) {}
            }
        }
    }

    # check if flag is correct
    CheckFlag(InAgent:agent):void = {
        # switch devices to array of bits (True/False)
        ParseInput()

        # exchange bits in InputBits to Exchanged
        ExchangeBits()

        # check flag
        for (i := 0..FlagBits.Length - 1) {
            if (b : logic = FlagBits[i]) {
                if (b <> Exchanged[Exchanged.Length-i-1]) {
                    Logger.Print("No")
                    return
                }
            }
        }

        # if correct, print flag to output!
        Logger.Print(BinaryToAscii(InputBits))
    }

    # bindings
    OnBegin<override>()<suspends>:void = {
        # when CheckFlagBtn is pressed, run CheckFlag function
        CheckFlagBtn.InteractedWithEvent.Subscribe(CheckFlag)
    }
}