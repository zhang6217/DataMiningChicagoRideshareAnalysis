import pandas as pd

rideshare_trips_df = pd.read_csv("~/rideshare_trips.csv")

columns_to_delete = ["Pickup Community Area",
                     "Dropoff Community Area",
                     "Shared Trip Authorized",
                     "Trips Pooled",
                     "Pickup Centroid Latitude",
                     "Pickup Centroid Longitude",
                     "Dropoff Centroid Latitude",
                     "Dropoff Centroid Longitude"]

new_column_names = ["trip_id", 
                    "start_timestamp_id", 
                    "end_timestamp_id", 
                    "duration_seconds", 
                    "miles", 
                    "start_census_tract", 
                    "end_census_tract", 
                    "fare", 
                    "tip",  
                    "extra_charges", 
                    "trip_total", 
                    "pickup_centroid_location",
                    "dropoff_centroid_location"]

rideshare_trips_df = rideshare_trips_df.drop(columns_to_delete, axis = 1)
rideshare_trips_df.columns = new_column_names

rideshare_trips_df.start_timestamp_id = pd.to_datetime(rideshare_trips_df.start_timestamp_id)
rideshare_trips_df.end_timestamp_id = pd.to_datetime(rideshare_trips_df.end_timestamp_id)

<<<<<<< HEAD
start_date = pd.to_datetime("2019-01-01")
end_date = pd.to_datetime("2019-12-31")
=======
start_date = "2019-01-01"
end_date = "2019-12-31"
>>>>>>> ce3566776f2680abea75ac3faa476fc11ba19b6c

between_two_dates = (rideshare_trips_df["start_timestamp_id"] >= start_date) & (rideshare_trips_df["end_timestamp_id"] <= end_date)
rideshare_trips_df = rideshare_trips_df.loc[between_two_dates]

rideshare_trips_df = rideshare_trips_df.sample(frac = 0.05, random_state = 272020)

rideshare_trips_df["tolls"] = 0
rideshare_trips_df["ride_type_id"] = 2
rideshare_trips_df["payment_type"] = "app"

rideshare_trips_df = rideshare_trips_df[["trip_id",
                                        "ride_type_id",
                                         "start_timestamp_id",
                                         "end_timestamp_id",
                                         "duration_seconds",
                                         "miles",
                                         "fare",
                                         "tip",
                                         "tolls",
                                         "extra_charges",
                                         "trip_total",
                                         "payment_type",
                                         "start_census_tract",
                                         "end_census_tract",
                                         "pickup_centroid_location",
                                         "dropoff_centroid_location"]]

<<<<<<< HEAD
=======

>>>>>>> ce3566776f2680abea75ac3faa476fc11ba19b6c
def hour_rounder(t):
  return (t.dt.floor('H'))

rideshare_trips_df.start_timestamp_id = hour_rounder(pd.to_datetime(rideshare_trips_df.start_timestamp_id))
rideshare_trips_df.end_timestamp_id = hour_rounder(pd.to_datetime(rideshare_trips_df.end_timestamp_id))

rideshare_trips_df.to_csv(r"~/clean_rideshare_trips.csv")
