import pandas as pd

test_files = ["000_mfqchildselfreportshort.txt",
"001_patienthealthquestionnaire.txt",
"004_newyorklongitudinalstudybythom.txt",
"005_beckdepressioninventorybdi.txt",
"006_apadsm5severitymeasurefordepre.txt",
"007_bhrcsselfreportedscared.txt",
"008_gad7anxietyupdated0.txt",
"009_validationoftheportugueseversi.txt",
"011_bhrcsparentreportsocialaptitud.txt",
"012_hrcw2protocolopsicoconfmenor18.txt",
"013_hrcw2protocolopsicoadultos.txt",
"014_testedeansiedadegad7dranadimme.txt",
"015_hrcw1dom.txt",
"016_hrcw2protocolodomiciliarmenor1.txt",
"019_bhrcsparentreportsocialcohesio.txt",
"021_sdqenglishukpt417single.txt",
"023_hrcw1psico.txt",
"024_bhrcsselfreportedmfq.txt",
"026_sf36.txt",
"030_bhrcsselfreportedwarwickedinbr.txt",
"031_ghq12.txt",
"032_bhrcsparentreportsdqchild.txt",
"034_bhrcsparentreportsocialcohesio.txt",
"037_hrcw0dom.txt",
"039_selfmeasuresforlonelinessandin.txt",
"045_mr0510201tb.txt",
"046_borderlinepersonalityscreener.txt",
"047_bhrcsparentreportsdqadult.txt",
"055_beta_retirement.txt",
"062_eoin_no_numbers.txt",
"064_hrcw1psicoconf.txt"]

ids = []
predictions = []
for test_file in test_files:
    with open("preprocessed_text/" + test_file, "r") as f:
        ids.append(test_file)
        predictions.append(f.read())
df = pd.DataFrame()
df["ID"] = ids
df["predict"] = predictions

df.to_csv("submission.csv", index=False)
