# Style_Transfer


## Style Transfert Principe

The principle of the style transfer is the following one:
  - We take 3 images : the style image, the content image and the input image
  - According to the weight we will attribute to the style or content we will have a different result
  
The input image is the combination of the style image and the content image
According to the weight we will attribute to the style or content image, we will have a different result.

![photo](https://github.com/Henri-Hoyez/Style_Transfer/blob/master/results/img2.jpg)

## Loss Funcitons

The loss is here to reduce distance between styles and contents

For that, we define 2 loss functions :
  - The Content loss 
  - The Style loss

We will try to minimize these 2 weighted losses

## Distances

It define the similarities between datas
Very important machine learning notion

## Content loss

We fed our model with our input image and our content image
We take, for each image, our model output features
We compute the mean square error between those features map


## Style loss

Weighted representation of the style difference between our input and style image
Compute the gram matrix of our feature layers
Compute the gram matrix of our style image feature
Compute the mean square error between them
Make this computation with several layers to increase the precision 


## Employed method

Classic Machine Meanring method
  - Data aquisition
  - Computing part
  - Results


## Data collection

We wrote an Instagram Scrapper to collect our images without signing in
We download few images in full size
Automatic scroll on the page before you signing in

## Computing part

 - Classic Classifier (VGG19)
 - Training loop
- Feed our classifier with the content and style image
- Compute the content and the style loss
- Backpropagate on our input image using LBFGS optimizer

## Find the best combinations

A script display a matrix with all the results according to the different styles

![photo](https://github.com/Henri-Hoyez/Style_Transfer/blob/master/results/Image1.png)

## Results 

  - Style image
  
 ![photo](https://github.com/Henri-Hoyez/Style_Transfer/blob/master/imgs/imgs/1.jpg)
  
  - Input image

![photo](https://github.com/Henri-Hoyez/Style_Transfer/blob/master/results/img3.jpg)
