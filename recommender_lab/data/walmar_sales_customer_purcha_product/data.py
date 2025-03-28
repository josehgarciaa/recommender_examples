import kagglehub

# Download latest version
path = kagglehub.dataset_download("devarajv88/walmart-sales-dataset")

print("Path to dataset files:", path)