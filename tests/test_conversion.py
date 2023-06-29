from healdata_utils.transforms.readstat.conversion import convert_readstat
import os


def compile_assertions(data1, data2):
    # helper function to bulk generate assertion statements for data structures.
    # data1: array of dicts -- this is the series of csvtemplate objects
    # data2: array of dicts -- this is the series of jsontemplate objects
    assertion_statements = ""
    for i, item in enumerate([data1, data2]):
        if i == 0:
            text = "csvtemplate_{}"
            var = "csv_template"
        else:
            text = "jsontemplate_{}"
            var = "json_template"
        for j, component in enumerate(item):
            assertion_statements += (
                "\n\n    " + text.format(str(j)) + "= {}".format(str(component))
            )
            assertion_statements += (
                "\n\n    assert {}[{}]".format(var, str(j)) + " == " + text.format(j)
            )
    with open(__file__, "r") as cur_file:
        test_file = cur_file.read()
        cur_file.close()
    lines = test_file.split("\n")

    for i, line in enumerate(lines):
        if line.replace(" ", "") == "##regexflagstart###":
            j = i
        elif line.replace(" ", "") == "##regexflagend###":
            n = i
    for x in range(n - j - 1):
        lines.pop(j + 1)
    new_text = ""
    for i, line in enumerate(lines):
        preamb = "" if i == 0 else "\n"
        if i == j + 1:
            new_text += "\n" + assertion_statements + "\n"
        new_text += preamb + line

    with open(__file__, "w") as cur_file:
        cur_file.write(new_text)
    print(os.getcwd())
    # os.system('cmd /k " venv\\Scripts\\activate"'.format(__file__))
    # os.system('cmd /c "black {}"'.format(__file__))
    return


def test_convert_readstat(compile_assertion=False):
    # compile_assertions: bool
    # use to bulk generate assertions statements for testing
    file_path = "tests/data/sas-nmhss-2019/data.sas7bdat"
    if os.path.isfile(file_path):
        print('file exists: regex')
    sas7bcat_file_path = "tests/data/sas-nmhss-2019/formats.sas7bcat"
    data_dictionaries = convert_readstat(
        file_path=file_path,
        data_dictionary_props={},
        sas7bcat_file_path=sas7bcat_file_path,
    )
    json_template = data_dictionaries["templatejson"]["data_dictionary"]
    csv_template = data_dictionaries["templatecsv"]["data_dictionary"]
    if compile_assertion:
        compile_assertions(csv_template, json_template)
        return
    ##regex flag start###

    csvtemplate_0 = {"name": "CASEID", "type": "integer"}

    assert csv_template[0] == csvtemplate_0

    csvtemplate_1 = {"name": "LST", "type": "string", "constraints.enum": "AK"}

    assert csv_template[1] == csvtemplate_1

    csvtemplate_2 = {
        "name": "MHINTAKE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[2] == csvtemplate_2

    csvtemplate_3 = {"name": "MHDIAGEVAL", "type": "number", "constraints.enum": "1.0"}

    assert csv_template[3] == csvtemplate_3

    csvtemplate_4 = {
        "name": "MHREFERRAL",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[4] == csvtemplate_4

    csvtemplate_5 = {
        "name": "SMISEDSUD",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[5] == csvtemplate_5

    csvtemplate_6 = {"name": "TREATMT", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[6] == csvtemplate_6

    csvtemplate_7 = {
        "name": "ADMINSERV",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[7] == csvtemplate_7

    csvtemplate_8 = {
        "name": "SETTINGIP",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[8] == csvtemplate_8

    csvtemplate_9 = {
        "name": "SETTINGRC",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[9] == csvtemplate_9

    csvtemplate_10 = {
        "name": "SETTINGDTPH",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[10] == csvtemplate_10

    csvtemplate_11 = {
        "name": "SETTINGOP",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[11] == csvtemplate_11

    csvtemplate_12 = {"name": "FACILITYTYPE", "type": "integer"}

    assert csv_template[12] == csvtemplate_12

    csvtemplate_13 = {
        "name": "FOCUS",
        "type": "number",
        "constraints.enum": "1.0|2.0|3.0|4.0|5.0",
        "encodings": "1.0=Mental health treatment|2.0=Substance abuse treatment|3.0=Mix of mental health and substance abuse treatment (neither is primary)|4.0=General health care|5.0=Other service focus",
        "description": "Primary treatment focus of facility",
    }

    assert csv_template[13] == csvtemplate_13

    csvtemplate_14 = {
        "name": "OWNERSHP",
        "type": "number",
        "constraints.enum": "1.0|2.0|3.0",
    }

    assert csv_template[14] == csvtemplate_14

    csvtemplate_15 = {"name": "PUBLICAGENCY", "type": "integer"}

    assert csv_template[15] == csvtemplate_15

    csvtemplate_16 = {
        "name": "TREATPSYCHOTHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
        "encodings": "0.0=No|1.0=Yes",
        "description": "Facility offers individual psychotherapy",
    }

    assert csv_template[16] == csvtemplate_16

    csvtemplate_17 = {
        "name": "TREATFAMTHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[17] == csvtemplate_17

    csvtemplate_18 = {
        "name": "TREATGRPTHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[18] == csvtemplate_18

    csvtemplate_19 = {
        "name": "TREATCOGTHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[19] == csvtemplate_19

    csvtemplate_20 = {
        "name": "TREATDIALTHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[20] == csvtemplate_20

    csvtemplate_21 = {
        "name": "TREATBEHAVMOD",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[21] == csvtemplate_21

    csvtemplate_22 = {
        "name": "TREATDUALMHSA",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[22] == csvtemplate_22

    csvtemplate_23 = {
        "name": "TREATTRAUMATHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
        "encodings": "0.0=No|1.0=Yes",
        "description": "Facility offers trauma therapy",
    }

    assert csv_template[23] == csvtemplate_23

    csvtemplate_24 = {
        "name": "TREATACTVTYTHRPY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[24] == csvtemplate_24

    csvtemplate_25 = {
        "name": "TREATELECTRO",
        "type": "number",
        "constraints.enum": "0.0",
    }

    assert csv_template[25] == csvtemplate_25

    csvtemplate_26 = {
        "name": "TREATTELEMEDINCE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[26] == csvtemplate_26

    csvtemplate_27 = {
        "name": "TREATPSYCHOMED",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[27] == csvtemplate_27

    csvtemplate_28 = {"name": "TREATOTH", "type": "number", "constraints.enum": "0.0"}

    assert csv_template[28] == csvtemplate_28

    csvtemplate_29 = {"name": "NOTREAT", "type": "number", "constraints.enum": "0.0"}

    assert csv_template[29] == csvtemplate_29

    csvtemplate_30 = {
        "name": "ASSERTCOMM",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[30] == csvtemplate_30

    csvtemplate_31 = {
        "name": "MHINTCASEMGMT",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[31] == csvtemplate_31

    csvtemplate_32 = {
        "name": "MHCASEMGMT",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[32] == csvtemplate_32

    csvtemplate_33 = {
        "name": "MHCOURTORDERED",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[33] == csvtemplate_33

    csvtemplate_34 = {
        "name": "MHCHRONIC",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[34] == csvtemplate_34

    csvtemplate_35 = {
        "name": "ILLNESSMGMT",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[35] == csvtemplate_35

    csvtemplate_36 = {
        "name": "PRIMARYCARE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[36] == csvtemplate_36

    csvtemplate_37 = {
        "name": "DIETEXERCOUNSEL",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[37] == csvtemplate_37

    csvtemplate_38 = {
        "name": "FAMPSYCHED",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[38] == csvtemplate_38

    csvtemplate_39 = {
        "name": "MHEDUCATION",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[39] == csvtemplate_39

    csvtemplate_40 = {
        "name": "MHHOUSING",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[40] == csvtemplate_40

    csvtemplate_41 = {
        "name": "SUPPHOUSING",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[41] == csvtemplate_41

    csvtemplate_42 = {
        "name": "MHPSYCHREHAB",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[42] == csvtemplate_42

    csvtemplate_43 = {
        "name": "MHVOCREHAB",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[43] == csvtemplate_43

    csvtemplate_44 = {
        "name": "SUPPEMPLOY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[44] == csvtemplate_44

    csvtemplate_45 = {
        "name": "FOSTERCARE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[45] == csvtemplate_45

    csvtemplate_46 = {
        "name": "MHLEGAL",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[46] == csvtemplate_46

    csvtemplate_47 = {
        "name": "MHEMGCY",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[47] == csvtemplate_47

    csvtemplate_48 = {
        "name": "MHSUICIDE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[48] == csvtemplate_48

    csvtemplate_49 = {
        "name": "MHCONSUMER",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[49] == csvtemplate_49

    csvtemplate_50 = {
        "name": "MHTOBACCOUSE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[50] == csvtemplate_50

    csvtemplate_51 = {
        "name": "MHTOBACCOCESS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[51] == csvtemplate_51

    csvtemplate_52 = {
        "name": "MHNICOTINEREP",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[52] == csvtemplate_52

    csvtemplate_53 = {
        "name": "SMOKINGCESSATION",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[53] == csvtemplate_53

    csvtemplate_54 = {"name": "MHOTH", "type": "number", "constraints.enum": "0.0"}

    assert csv_template[54] == csvtemplate_54

    csvtemplate_55 = {
        "name": "MHNOSVCS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[55] == csvtemplate_55

    csvtemplate_56 = {
        "name": "CHILDAD",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[56] == csvtemplate_56

    csvtemplate_57 = {"name": "ADOLES", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[57] == csvtemplate_57

    csvtemplate_58 = {
        "name": "YOUNGADULTS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
        "encodings": "0.0=No|1.0=Yes",
        "description": "Accepts young adults (aged 18-25 years old) for Tx",
    }

    assert csv_template[58] == csvtemplate_58

    csvtemplate_59 = {"name": "ADULT", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[59] == csvtemplate_59

    csvtemplate_60 = {
        "name": "SENIORS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[60] == csvtemplate_60

    csvtemplate_61 = {"name": "SED", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[61] == csvtemplate_61

    csvtemplate_62 = {
        "name": "TAYOUNGADULTS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[62] == csvtemplate_62

    csvtemplate_63 = {"name": "SPMI", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[63] == csvtemplate_63

    csvtemplate_64 = {"name": "SRVC63", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[64] == csvtemplate_64

    csvtemplate_65 = {
        "name": "ALZHDEMENTIA",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[65] == csvtemplate_65

    csvtemplate_66 = {"name": "SRVC31", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[66] == csvtemplate_66

    csvtemplate_67 = {
        "name": "SPECGRPEATING",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[67] == csvtemplate_67

    csvtemplate_68 = {
        "name": "POSTTRAUM",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[68] == csvtemplate_68

    csvtemplate_69 = {
        "name": "SRVC116",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[69] == csvtemplate_69

    csvtemplate_70 = {
        "name": "TRAUMATICBRAIN",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[70] == csvtemplate_70

    csvtemplate_71 = {
        "name": "SRVC113",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[71] == csvtemplate_71

    csvtemplate_72 = {
        "name": "SRVC114",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[72] == csvtemplate_72

    csvtemplate_73 = {
        "name": "SRVC115",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[73] == csvtemplate_73

    csvtemplate_74 = {"name": "SRVC62", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[74] == csvtemplate_74

    csvtemplate_75 = {"name": "SRVC61", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[75] == csvtemplate_75

    csvtemplate_76 = {"name": "SRVC32", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[76] == csvtemplate_76

    csvtemplate_77 = {"name": "SRVC35", "type": "number", "constraints.enum": "0.0"}

    assert csv_template[77] == csvtemplate_77

    csvtemplate_78 = {
        "name": "NOSPECGRP",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[78] == csvtemplate_78

    csvtemplate_79 = {
        "name": "CRISISTEAM2",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[79] == csvtemplate_79

    csvtemplate_80 = {
        "name": "SIGNLANG",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[80] == csvtemplate_80

    csvtemplate_81 = {"name": "LANG", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[81] == csvtemplate_81

    csvtemplate_82 = {"name": "LANGPROV", "type": "integer"}

    assert csv_template[82] == csvtemplate_82

    csvtemplate_83 = {
        "name": "LANG16",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[83] == csvtemplate_83

    csvtemplate_84 = {
        "name": "LANG_B",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[84] == csvtemplate_84

    csvtemplate_85 = {"name": "LANG1", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[85] == csvtemplate_85

    csvtemplate_86 = {"name": "LANG2", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[86] == csvtemplate_86

    csvtemplate_87 = {"name": "LANG3", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[87] == csvtemplate_87

    csvtemplate_88 = {
        "name": "LANG21",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[88] == csvtemplate_88

    csvtemplate_89 = {"name": "LANG4", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[89] == csvtemplate_89

    csvtemplate_90 = {"name": "LANG5", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[90] == csvtemplate_90

    csvtemplate_91 = {"name": "LANG6", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[91] == csvtemplate_91

    csvtemplate_92 = {"name": "LANG7", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[92] == csvtemplate_92

    csvtemplate_93 = {"name": "LANG8", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[93] == csvtemplate_93

    csvtemplate_94 = {
        "name": "LANG24",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[94] == csvtemplate_94

    csvtemplate_95 = {"name": "LANG9", "type": "number", "constraints.enum": "-2.0|0.0"}

    assert csv_template[95] == csvtemplate_95

    csvtemplate_96 = {
        "name": "LANG10",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[96] == csvtemplate_96

    csvtemplate_97 = {
        "name": "LANG22",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[97] == csvtemplate_97

    csvtemplate_98 = {
        "name": "LANG25",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[98] == csvtemplate_98

    csvtemplate_99 = {
        "name": "LANG26",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[99] == csvtemplate_99

    csvtemplate_100 = {
        "name": "LANG11",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[100] == csvtemplate_100

    csvtemplate_101 = {
        "name": "LANG19",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[101] == csvtemplate_101

    csvtemplate_102 = {
        "name": "LANG23",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[102] == csvtemplate_102

    csvtemplate_103 = {
        "name": "LANG12",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[103] == csvtemplate_103

    csvtemplate_104 = {
        "name": "LANG13",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[104] == csvtemplate_104

    csvtemplate_105 = {
        "name": "LANG14",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[105] == csvtemplate_105

    csvtemplate_106 = {
        "name": "LANG15",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[106] == csvtemplate_106

    csvtemplate_107 = {
        "name": "LANG20",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[107] == csvtemplate_107

    csvtemplate_108 = {
        "name": "LANG17",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[108] == csvtemplate_108

    csvtemplate_109 = {
        "name": "LANG18",
        "type": "number",
        "constraints.enum": "-2.0|0.0",
    }

    assert csv_template[109] == csvtemplate_109

    csvtemplate_110 = {
        "name": "SMOKINGPOLICY",
        "type": "number",
        "constraints.enum": "1.0|2.0",
    }

    assert csv_template[110] == csvtemplate_110

    csvtemplate_111 = {
        "name": "FEESCALE",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[111] == csvtemplate_111

    csvtemplate_112 = {
        "name": "PAYASST",
        "type": "number",
        "constraints.enum": "-2.0|0.0|1.0",
    }

    assert csv_template[112] == csvtemplate_112

    csvtemplate_113 = {
        "name": "REVCHK1",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[113] == csvtemplate_113

    csvtemplate_114 = {
        "name": "REVCHK2",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[114] == csvtemplate_114

    csvtemplate_115 = {
        "name": "REVCHK8",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[115] == csvtemplate_115

    csvtemplate_116 = {
        "name": "REVCHK5",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[116] == csvtemplate_116

    csvtemplate_117 = {
        "name": "REVCHK10",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[117] == csvtemplate_117

    csvtemplate_118 = {
        "name": "FUNDSMHA",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[118] == csvtemplate_118

    csvtemplate_119 = {
        "name": "FUNDSTATEWELFARE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[119] == csvtemplate_119

    csvtemplate_120 = {
        "name": "FUNDSTATEJUV",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[120] == csvtemplate_120

    csvtemplate_121 = {
        "name": "FUNDSTATEEDUC",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[121] == csvtemplate_121

    csvtemplate_122 = {
        "name": "FUNDOTHSTATE",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[122] == csvtemplate_122

    csvtemplate_123 = {
        "name": "FUNDLOCALGOV",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[123] == csvtemplate_123

    csvtemplate_124 = {
        "name": "FUNDCSBG",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[124] == csvtemplate_124

    csvtemplate_125 = {
        "name": "FUNDCMHG",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[125] == csvtemplate_125

    csvtemplate_126 = {
        "name": "REVCHK15",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[126] == csvtemplate_126

    csvtemplate_127 = {
        "name": "FUNDVA",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[127] == csvtemplate_127

    csvtemplate_128 = {
        "name": "REVCHK17",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[128] == csvtemplate_128

    csvtemplate_129 = {"name": "REVCHK2A", "type": "number", "constraints.enum": "0.0"}

    assert csv_template[129] == csvtemplate_129

    csvtemplate_130 = {
        "name": "LICENMH",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[130] == csvtemplate_130

    csvtemplate_131 = {
        "name": "LICENSED",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[131] == csvtemplate_131

    csvtemplate_132 = {
        "name": "LICENPH",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[132] == csvtemplate_132

    csvtemplate_133 = {
        "name": "LICENSEDFCS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[133] == csvtemplate_133

    csvtemplate_134 = {
        "name": "LICENHOS",
        "type": "number",
        "constraints.enum": "0.0|1.0",
    }

    assert csv_template[134] == csvtemplate_134

    csvtemplate_135 = {"name": "JCAHO", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[135] == csvtemplate_135

    csvtemplate_136 = {"name": "CARF", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[136] == csvtemplate_136

    csvtemplate_137 = {"name": "COA", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[137] == csvtemplate_137

    csvtemplate_138 = {"name": "CMS", "type": "number", "constraints.enum": "0.0|1.0"}

    assert csv_template[138] == csvtemplate_138

    csvtemplate_139 = {"name": "OTHSTATE", "type": "number", "constraints.enum": "0.0"}

    assert csv_template[139] == csvtemplate_139

    jsontemplate_0 = {"name": "CASEID", "type": "integer"}

    assert json_template[0] == jsontemplate_0

    jsontemplate_1 = {"name": "LST", "type": "string", "constraints": {"enum": ["AK"]}}

    assert json_template[1] == jsontemplate_1

    jsontemplate_2 = {
        "name": "MHINTAKE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[2] == jsontemplate_2

    jsontemplate_3 = {
        "name": "MHDIAGEVAL",
        "type": "number",
        "constraints": {"enum": [1.0]},
    }

    assert json_template[3] == jsontemplate_3

    jsontemplate_4 = {
        "name": "MHREFERRAL",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[4] == jsontemplate_4

    jsontemplate_5 = {
        "name": "SMISEDSUD",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[5] == jsontemplate_5

    jsontemplate_6 = {
        "name": "TREATMT",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[6] == jsontemplate_6

    jsontemplate_7 = {
        "name": "ADMINSERV",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[7] == jsontemplate_7

    jsontemplate_8 = {
        "name": "SETTINGIP",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[8] == jsontemplate_8

    jsontemplate_9 = {
        "name": "SETTINGRC",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[9] == jsontemplate_9

    jsontemplate_10 = {
        "name": "SETTINGDTPH",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[10] == jsontemplate_10

    jsontemplate_11 = {
        "name": "SETTINGOP",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[11] == jsontemplate_11

    jsontemplate_12 = {"name": "FACILITYTYPE", "type": "integer"}

    assert json_template[12] == jsontemplate_12

    jsontemplate_13 = {
        "name": "FOCUS",
        "type": "number",
        "constraints": {"enum": ["1.0", "2.0", "3.0", "4.0", "5.0"]},
        "encodings": {
            1.0: "Mental health treatment",
            2.0: "Substance abuse treatment",
            3.0: "Mix of mental health and substance abuse treatment (neither is primary)",
            4.0: "General health care",
            5.0: "Other service focus",
        },
        "description": "Primary treatment focus of facility",
    }

    assert json_template[13] == jsontemplate_13

    jsontemplate_14 = {
        "name": "OWNERSHP",
        "type": "number",
        "constraints": {"enum": [1.0, 2.0, 3.0]},
    }

    assert json_template[14] == jsontemplate_14

    jsontemplate_15 = {"name": "PUBLICAGENCY", "type": "integer"}

    assert json_template[15] == jsontemplate_15

    jsontemplate_16 = {
        "name": "TREATPSYCHOTHRPY",
        "type": "number",
        "constraints": {"enum": ["0.0", "1.0"]},
        "encodings": {0.0: "No", 1.0: "Yes"},
        "description": "Facility offers individual psychotherapy",
    }

    assert json_template[16] == jsontemplate_16

    jsontemplate_17 = {
        "name": "TREATFAMTHRPY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[17] == jsontemplate_17

    jsontemplate_18 = {
        "name": "TREATGRPTHRPY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[18] == jsontemplate_18

    jsontemplate_19 = {
        "name": "TREATCOGTHRPY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[19] == jsontemplate_19

    jsontemplate_20 = {
        "name": "TREATDIALTHRPY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[20] == jsontemplate_20

    jsontemplate_21 = {
        "name": "TREATBEHAVMOD",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[21] == jsontemplate_21

    jsontemplate_22 = {
        "name": "TREATDUALMHSA",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[22] == jsontemplate_22

    jsontemplate_23 = {
        "name": "TREATTRAUMATHRPY",
        "type": "number",
        "constraints": {"enum": ["0.0", "1.0"]},
        "encodings": {0.0: "No", 1.0: "Yes"},
        "description": "Facility offers trauma therapy",
    }

    assert json_template[23] == jsontemplate_23

    jsontemplate_24 = {
        "name": "TREATACTVTYTHRPY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[24] == jsontemplate_24

    jsontemplate_25 = {
        "name": "TREATELECTRO",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[25] == jsontemplate_25

    jsontemplate_26 = {
        "name": "TREATTELEMEDINCE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[26] == jsontemplate_26

    jsontemplate_27 = {
        "name": "TREATPSYCHOMED",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[27] == jsontemplate_27

    jsontemplate_28 = {
        "name": "TREATOTH",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[28] == jsontemplate_28

    jsontemplate_29 = {
        "name": "NOTREAT",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[29] == jsontemplate_29

    jsontemplate_30 = {
        "name": "ASSERTCOMM",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[30] == jsontemplate_30

    jsontemplate_31 = {
        "name": "MHINTCASEMGMT",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[31] == jsontemplate_31

    jsontemplate_32 = {
        "name": "MHCASEMGMT",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[32] == jsontemplate_32

    jsontemplate_33 = {
        "name": "MHCOURTORDERED",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[33] == jsontemplate_33

    jsontemplate_34 = {
        "name": "MHCHRONIC",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[34] == jsontemplate_34

    jsontemplate_35 = {
        "name": "ILLNESSMGMT",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[35] == jsontemplate_35

    jsontemplate_36 = {
        "name": "PRIMARYCARE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[36] == jsontemplate_36

    jsontemplate_37 = {
        "name": "DIETEXERCOUNSEL",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[37] == jsontemplate_37

    jsontemplate_38 = {
        "name": "FAMPSYCHED",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[38] == jsontemplate_38

    jsontemplate_39 = {
        "name": "MHEDUCATION",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[39] == jsontemplate_39

    jsontemplate_40 = {
        "name": "MHHOUSING",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[40] == jsontemplate_40

    jsontemplate_41 = {
        "name": "SUPPHOUSING",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[41] == jsontemplate_41

    jsontemplate_42 = {
        "name": "MHPSYCHREHAB",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[42] == jsontemplate_42

    jsontemplate_43 = {
        "name": "MHVOCREHAB",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[43] == jsontemplate_43

    jsontemplate_44 = {
        "name": "SUPPEMPLOY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[44] == jsontemplate_44

    jsontemplate_45 = {
        "name": "FOSTERCARE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[45] == jsontemplate_45

    jsontemplate_46 = {
        "name": "MHLEGAL",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[46] == jsontemplate_46

    jsontemplate_47 = {
        "name": "MHEMGCY",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[47] == jsontemplate_47

    jsontemplate_48 = {
        "name": "MHSUICIDE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[48] == jsontemplate_48

    jsontemplate_49 = {
        "name": "MHCONSUMER",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[49] == jsontemplate_49

    jsontemplate_50 = {
        "name": "MHTOBACCOUSE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[50] == jsontemplate_50

    jsontemplate_51 = {
        "name": "MHTOBACCOCESS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[51] == jsontemplate_51

    jsontemplate_52 = {
        "name": "MHNICOTINEREP",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[52] == jsontemplate_52

    jsontemplate_53 = {
        "name": "SMOKINGCESSATION",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[53] == jsontemplate_53

    jsontemplate_54 = {
        "name": "MHOTH",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[54] == jsontemplate_54

    jsontemplate_55 = {
        "name": "MHNOSVCS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[55] == jsontemplate_55

    jsontemplate_56 = {
        "name": "CHILDAD",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[56] == jsontemplate_56

    jsontemplate_57 = {
        "name": "ADOLES",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[57] == jsontemplate_57

    jsontemplate_58 = {
        "name": "YOUNGADULTS",
        "type": "number",
        "constraints": {"enum": ["0.0", "1.0"]},
        "encodings": {0.0: "No", 1.0: "Yes"},
        "description": "Accepts young adults (aged 18-25 years old) for Tx",
    }

    assert json_template[58] == jsontemplate_58

    jsontemplate_59 = {
        "name": "ADULT",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[59] == jsontemplate_59

    jsontemplate_60 = {
        "name": "SENIORS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[60] == jsontemplate_60

    jsontemplate_61 = {
        "name": "SED",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[61] == jsontemplate_61

    jsontemplate_62 = {
        "name": "TAYOUNGADULTS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[62] == jsontemplate_62

    jsontemplate_63 = {
        "name": "SPMI",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[63] == jsontemplate_63

    jsontemplate_64 = {
        "name": "SRVC63",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[64] == jsontemplate_64

    jsontemplate_65 = {
        "name": "ALZHDEMENTIA",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[65] == jsontemplate_65

    jsontemplate_66 = {
        "name": "SRVC31",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[66] == jsontemplate_66

    jsontemplate_67 = {
        "name": "SPECGRPEATING",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[67] == jsontemplate_67

    jsontemplate_68 = {
        "name": "POSTTRAUM",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[68] == jsontemplate_68

    jsontemplate_69 = {
        "name": "SRVC116",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[69] == jsontemplate_69

    jsontemplate_70 = {
        "name": "TRAUMATICBRAIN",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[70] == jsontemplate_70

    jsontemplate_71 = {
        "name": "SRVC113",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[71] == jsontemplate_71

    jsontemplate_72 = {
        "name": "SRVC114",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[72] == jsontemplate_72

    jsontemplate_73 = {
        "name": "SRVC115",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[73] == jsontemplate_73

    jsontemplate_74 = {
        "name": "SRVC62",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[74] == jsontemplate_74

    jsontemplate_75 = {
        "name": "SRVC61",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[75] == jsontemplate_75

    jsontemplate_76 = {
        "name": "SRVC32",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[76] == jsontemplate_76

    jsontemplate_77 = {
        "name": "SRVC35",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[77] == jsontemplate_77

    jsontemplate_78 = {
        "name": "NOSPECGRP",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[78] == jsontemplate_78

    jsontemplate_79 = {
        "name": "CRISISTEAM2",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[79] == jsontemplate_79

    jsontemplate_80 = {
        "name": "SIGNLANG",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[80] == jsontemplate_80

    jsontemplate_81 = {
        "name": "LANG",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[81] == jsontemplate_81

    jsontemplate_82 = {"name": "LANGPROV", "type": "integer"}

    assert json_template[82] == jsontemplate_82

    jsontemplate_83 = {
        "name": "LANG16",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[83] == jsontemplate_83

    jsontemplate_84 = {
        "name": "LANG_B",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[84] == jsontemplate_84

    jsontemplate_85 = {
        "name": "LANG1",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[85] == jsontemplate_85

    jsontemplate_86 = {
        "name": "LANG2",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[86] == jsontemplate_86

    jsontemplate_87 = {
        "name": "LANG3",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[87] == jsontemplate_87

    jsontemplate_88 = {
        "name": "LANG21",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[88] == jsontemplate_88

    jsontemplate_89 = {
        "name": "LANG4",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[89] == jsontemplate_89

    jsontemplate_90 = {
        "name": "LANG5",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[90] == jsontemplate_90

    jsontemplate_91 = {
        "name": "LANG6",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[91] == jsontemplate_91

    jsontemplate_92 = {
        "name": "LANG7",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[92] == jsontemplate_92

    jsontemplate_93 = {
        "name": "LANG8",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[93] == jsontemplate_93

    jsontemplate_94 = {
        "name": "LANG24",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[94] == jsontemplate_94

    jsontemplate_95 = {
        "name": "LANG9",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[95] == jsontemplate_95

    jsontemplate_96 = {
        "name": "LANG10",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[96] == jsontemplate_96

    jsontemplate_97 = {
        "name": "LANG22",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[97] == jsontemplate_97

    jsontemplate_98 = {
        "name": "LANG25",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[98] == jsontemplate_98

    jsontemplate_99 = {
        "name": "LANG26",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[99] == jsontemplate_99

    jsontemplate_100 = {
        "name": "LANG11",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[100] == jsontemplate_100

    jsontemplate_101 = {
        "name": "LANG19",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[101] == jsontemplate_101

    jsontemplate_102 = {
        "name": "LANG23",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[102] == jsontemplate_102

    jsontemplate_103 = {
        "name": "LANG12",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[103] == jsontemplate_103

    jsontemplate_104 = {
        "name": "LANG13",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[104] == jsontemplate_104

    jsontemplate_105 = {
        "name": "LANG14",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[105] == jsontemplate_105

    jsontemplate_106 = {
        "name": "LANG15",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[106] == jsontemplate_106

    jsontemplate_107 = {
        "name": "LANG20",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[107] == jsontemplate_107

    jsontemplate_108 = {
        "name": "LANG17",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[108] == jsontemplate_108

    jsontemplate_109 = {
        "name": "LANG18",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0]},
    }

    assert json_template[109] == jsontemplate_109

    jsontemplate_110 = {
        "name": "SMOKINGPOLICY",
        "type": "number",
        "constraints": {"enum": [1.0, 2.0]},
    }

    assert json_template[110] == jsontemplate_110

    jsontemplate_111 = {
        "name": "FEESCALE",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[111] == jsontemplate_111

    jsontemplate_112 = {
        "name": "PAYASST",
        "type": "number",
        "constraints": {"enum": [-2.0, 0.0, 1.0]},
    }

    assert json_template[112] == jsontemplate_112

    jsontemplate_113 = {
        "name": "REVCHK1",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[113] == jsontemplate_113

    jsontemplate_114 = {
        "name": "REVCHK2",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[114] == jsontemplate_114

    jsontemplate_115 = {
        "name": "REVCHK8",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[115] == jsontemplate_115

    jsontemplate_116 = {
        "name": "REVCHK5",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[116] == jsontemplate_116

    jsontemplate_117 = {
        "name": "REVCHK10",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[117] == jsontemplate_117

    jsontemplate_118 = {
        "name": "FUNDSMHA",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[118] == jsontemplate_118

    jsontemplate_119 = {
        "name": "FUNDSTATEWELFARE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[119] == jsontemplate_119

    jsontemplate_120 = {
        "name": "FUNDSTATEJUV",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[120] == jsontemplate_120

    jsontemplate_121 = {
        "name": "FUNDSTATEEDUC",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[121] == jsontemplate_121

    jsontemplate_122 = {
        "name": "FUNDOTHSTATE",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[122] == jsontemplate_122

    jsontemplate_123 = {
        "name": "FUNDLOCALGOV",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[123] == jsontemplate_123

    jsontemplate_124 = {
        "name": "FUNDCSBG",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[124] == jsontemplate_124

    jsontemplate_125 = {
        "name": "FUNDCMHG",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[125] == jsontemplate_125

    jsontemplate_126 = {
        "name": "REVCHK15",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[126] == jsontemplate_126

    jsontemplate_127 = {
        "name": "FUNDVA",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[127] == jsontemplate_127

    jsontemplate_128 = {
        "name": "REVCHK17",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[128] == jsontemplate_128

    jsontemplate_129 = {
        "name": "REVCHK2A",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[129] == jsontemplate_129

    jsontemplate_130 = {
        "name": "LICENMH",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[130] == jsontemplate_130

    jsontemplate_131 = {
        "name": "LICENSED",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[131] == jsontemplate_131

    jsontemplate_132 = {
        "name": "LICENPH",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[132] == jsontemplate_132

    jsontemplate_133 = {
        "name": "LICENSEDFCS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[133] == jsontemplate_133

    jsontemplate_134 = {
        "name": "LICENHOS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[134] == jsontemplate_134

    jsontemplate_135 = {
        "name": "JCAHO",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[135] == jsontemplate_135

    jsontemplate_136 = {
        "name": "CARF",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[136] == jsontemplate_136

    jsontemplate_137 = {
        "name": "COA",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[137] == jsontemplate_137

    jsontemplate_138 = {
        "name": "CMS",
        "type": "number",
        "constraints": {"enum": [0.0, 1.0]},
    }

    assert json_template[138] == jsontemplate_138

    jsontemplate_139 = {
        "name": "OTHSTATE",
        "type": "number",
        "constraints": {"enum": [0.0]},
    }

    assert json_template[139] == jsontemplate_139

    ##regex flag end###