import pandas as pd

units = pd.read_table("units.tsv", index_col=["sample","unit"], dtype=str)

# works, is not pythonic
# for i in enumerate(units.index):
#     if i[1][1].startswith("SRR"):
#         print(i[1][1])

# returns generator object instead of output
# print(i[1][1] for i in enumerate(units.index) if i[1][1].startswith("SRR"))

# Should work in a Snakemake framework. Try other things as long as I'm at it.
# def get_SRRid():
# #     return(i[1][1] for i in enumerate(units.index) if i[1][1].startswith("SRR"))
#     srrIDs = []
#     for i in enumerate(units.index):
#         if i[1][1].startswith("SRR"):
#             srrIDs.append(i[1][1])
#     return srrIDs
# 
# print(get_SRRid())

# def get_SRRid():
#     srrIDs = []
#     for i in units.index:
#         if i[1].startswith("SRR"):
#             srrIDs.append(i[1])
#     return srrIDs
#     
# print(get_SRRid())


# print("data/reads/"+units[["fq1","fq2"]])