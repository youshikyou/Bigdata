# Read timestamp convert into int
# Add new columns for timestamp features day, hour, minute, and second
df1 = df.copy()
df1['day'] = df1['click_time'].dt.day.astype('uint8')
df1['hour'] = df1['click_time'].dt.hour.astype('uint8')
