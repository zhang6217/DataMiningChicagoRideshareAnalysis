import pandas as pd

regions_df = pd.read_csv("~/regions.csv")

regions_df.rename(columns = {'REGIONID':'region_id'}, inplace = True)

regions_df.columns = map(str.lower, regions_df.columns)

regions_df.columns = regions_df.columns.to_series().apply(lambda x: x.strip())

#regions_df = regions_df.drop(["current_speed","last_updated","description", "east", "south"], axis = 1)

regions_df = regions_df[["region_id","region","nw_location","se_location"]]

regions_df.drop_duplicates(inplace = True)

# Create empty columns for lats and longs
regions_df["lat_nw"] = ""
regions_df["long_nw"] = ""
regions_df["lat_se"] = ""
regions_df["long_se"] = ""

# Fill empty columns
for row in range(len(regions_df.index)):

    # NW latitude
    start = regions_df.iloc[row, 2].find("(") + 1
    end = regions_df.iloc[row, 2].find(" ", 6)
    regions_df.iloc[row, 4] = float(regions_df.iloc[row, 2][start:end])

    # NW longitude
    start = regions_df.iloc[row, 2].find(" ", 6) + 1
    end = regions_df.iloc[row, 2].find(")")
    regions_df.iloc[row, 5] = float(regions_df.iloc[row, 2][start:end])

    # SE latitude
    start = regions_df.iloc[row, 3].find("(") + 1
    end = regions_df.iloc[row, 3].find(" ", 6)
    regions_df.iloc[row, 6] = float(regions_df.iloc[row, 3][start:end])

    # SE longitude
    start = regions_df.iloc[row, 3].find(" ", 6) + 1
    end = regions_df.iloc[row, 3].find(")")
    regions_df.iloc[row, 7] = float(regions_df.iloc[row, 3][start:end])

# Compute centroids
regions_df["lat_centroid"] = (regions_df.lat_nw+regions_df.lat_se)/2
regions_df["long_centroid"] = (regions_df.long_nw+regions_df.long_se)/2

# Keep only relevant columns
regions_df = regions_df[["region_id","region","lat_centroid", "long_centroid"]]

regions_df.to_csv(r"~/clean_regions.csv", index = False) # To be used in other calculations

regions_df.to_csv(r"~/headerless_clean_regions.csv", index = False, header = False) # Actual DW table for dim_base_region
