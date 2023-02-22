import pandas as pd

PATH = "/Users/junyuwu/Housing price/component/kc_house_data.csv"
df = pd.read_csv(PATH)

def get_data():
    return df

def get_bed():
    bybedrooms = df.groupby("bedrooms")["price"].mean()
    bybedrooms = bybedrooms[:12]
    listbed =list(set(bybedrooms.index.tolist()))    
    return listbed

def get_bath():
    bybathrooms = df.groupby("bathrooms")["price"].mean()
    listbath =list(set(bybathrooms.index.tolist()))  
    return listbath

def get_floor():
    byfloors = df.groupby("floors")["price"].mean()
    listfloor =list(set(byfloors.index.tolist())) 
    return listfloor

def get_bed_price():
    bybedrooms = df.groupby("bedrooms")["price"].mean()
    bybedrooms = bybedrooms[:12].to_frame()
    bybedrooms.reset_index(inplace=True)
    return bybedrooms

def get_bath_price():
    bybathrooms = df.groupby("bathrooms")["price"].mean().to_frame()
    bybathrooms.reset_index(inplace=True)
    return bybathrooms

def get_floor_price():
    byfloors = df.groupby("floors")["price"].mean().to_frame()
    byfloors.reset_index(inplace=True)
    return byfloors

def get_base_price():
    bybase = df.groupby("sqft_basement")["price"].mean().to_frame()
    bybase.reset_index(inplace=True)
    return bybase

def get_condition_price():
    bycondition = df.groupby("condition")["price"].mean().to_frame()
    bycondition.reset_index(inplace=True)
    return bycondition

def get_year():
    byyear = df.groupby("yr_built")["price"].mean().sort_values(ascending=False)[:150].to_frame()
    byyear.reset_index(inplace=True)
    return byyear

def get_view():
    byview = df["view"].value_counts().to_frame()
    byview.reset_index(inplace=True)
    return byview