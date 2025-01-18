# Check if the module import works
try:
    from keras.layers import LegacyLayerName
except ImportError as e:
    print("Error importing LegacyLayerName:", e)
