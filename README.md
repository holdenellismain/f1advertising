# F1 Advertising Space Analysis

## Goals

Billions of dollars are spent on advertising during F1 races throughout the year. A key part of this is the ads that are painted onto the cars driven in each race. This project studies which parts of the car have the most exposure on the broadcast and other forms of F1 media.

## Skills/Tools Used

- PyTorch (CNN)
- Python to scrape frames from YouTube
- R (ggplot2) for data visualization

## Steps
### Data Collection
1. [extract_frame.py](code/extract_frame.py) uses yt-dlp to download YouTube highlights of F1 races
2. [label.py](code/label.py) is used to manually label frames
3. [splitdata.ipynb](code/splitdata.ipynb) sorts and balances images into the structure expected by [ImageFolder](https://docs.pytorch.org/vision/main/generated/torchvision.datasets.ImageFolder.html)
4. Augment the training data using [augment_crop.py](code/augment_crop.py) and [augment_noise.py](code/augment_noise.py)

### Modelling
- Experimented with many architectures such as a two-level classification model.
- Training metrics were based on a separate validation set to avoid overfitting.
- Ended up using ResNet-18, initializing training with the pre-existing weights (detail in [pretrained.ipynb](code/pretrained.ipynb))
- For frame-by-frame classification I used mode filtering to smooth out prediction noise (detail in [resnet_prediction_by_frame.ipynb](code/resnet_prediction_by_frame.ipynb))

### Results

Our final model had a validation accuracy of around 85% and was able to identify the inside/cockpit camera angle correctly over 97% of the time. Lots of innacuracy was due to subjectivity in the labelling (i.e. whether a car is "distant" or not)

![confusion](https://github.com/user-attachments/assets/829c0397-426e-4809-8a55-26784ebe75a2)

Our main result was that as content get shorter, the inside of the car is shown more and the rear of the car is shown less. For advertisers, this means that even though the inside is not shown very often on the full race broadcast, it is an effective placement to reach younger generations for social media. On the other hand, ads on the rear of the car are a good way to target race enthusiasts.

![proprtions](https://github.com/user-attachments/assets/e10ad095-6b09-48e3-af3f-a66172ef3ea3)

We also looked into the distribution of angle by track using [resnet_prediction_by_race.ipynb](code/resnet_prediction_by_race.ipynb) and [plots.rmd](code/plots.Rmd) and the distributions did vary, but we could not make any recommendations.



