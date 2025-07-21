import os
import argparse
from pyiqa import create_metric
from PIL import Image
import numpy as np
import torchvision.transforms as transforms
from tqdm import tqdm

# Define a dictionary to map metric names to pyiqa metric functions
METRIC_FUNCTIONS = {
    'niqe': 'niqe',
    'musiq': 'musiq',
    'pi': 'pi',
    'brisque': 'brisque',
    'nrqm': 'nrqm',
    'maniqa': 'maniqa',
    'clipiqa': 'clipiqa',
    'clipiqa+': 'clipiqa+'
}

def calculate_metric(image, metric):
    
    # Calculate the metric for the given image
    score = metric(image)
    
    return score.item()

def load_image(image_path):
    # Load image using PIL and convert it to RGB (in case it's not)
    image = Image.open(image_path).convert('RGB')

    # Create a transform to convert the image to a tenso
    convert_tensor = transforms.ToTensor()
    
    # Convert the PIL image to a NumPy array
    #image_np = np.array(image) / 255.
    #image_np =image_np.astype(np.float32)

    return convert_tensor(image).unsqueeze(0)

def process_folder(folder_path, metrics):
    scores = {metric_name: [] for metric_name in metrics}

    # Calculate and store each selected metric for the image
    for metric_name in tqdm(metrics):

        # Create the metric object using pyiqa
        metric = create_metric(METRIC_FUNCTIONS[metric_name])
    
        # Iterate over all files in the folder
        for image_file in tqdm(os.listdir(folder_path)):
            # Construct full path to the image
            image_path = os.path.join(folder_path, image_file)
            
            # Check if the file is an image (we'll assume common image extensions)
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                
                # Load the image
                image = load_image(image_path)
                #print(f"Processing {image_path} ...", image.shape)
                score = calculate_metric(image, metric)
                scores[metric_name].append(score)

        print (metric_name, np.mean(scores[metric_name]), len(scores[metric_name]) )
        print ()

    # Compute the average for each metric
    avg_scores = {metric_name: np.mean(scores[metric_name]) for metric_name in metrics}
    return avg_scores

def main():
    # Argument parser for command-line options
    parser = argparse.ArgumentParser(description="Calculate blind image quality metrics for a folder of images.")
    
    parser.add_argument('--folder', type=str, required=True, help="Path to the folder containing images.")
    parser.add_argument('--metrics', type=str, nargs='+', required=True, choices=METRIC_FUNCTIONS.keys(),
                        help="List of metrics to calculate (choose from: 'niqe', 'musiq', 'pi', 'brisque', 'nrqm', 'maniqa', 'clipiqa', 'clipiqa+').")
    
    args = parser.parse_args()
    
    # Check if folder exists
    if not os.path.isdir(args.folder):
        print(f"Error: Folder {args.folder} does not exist.")
        return
    
    # Process the folder and calculate the metrics
    avg_scores = process_folder(args.folder, args.metrics)
    
    # Print the average scores for each selected metric
    print("\nAverage quality scores for the dataset:")
    for metric, score in avg_scores.items():
        print(f"{metric.upper()}: {score:.4f}")

if __name__ == '__main__':
    main()