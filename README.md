# MMR Predictor

## Introduction
<!-- What deep learning model are you building? We are looking for a clear and concise description that uses standard deep learning terminology. Clearly describe the type of task that you are solving, and what your input/outputs are. -->

MMR Predictor is a recurrent neural network model that uses LSTM architecture to do a multi-class classification task. In this model, we introduce 7 classes of ELO rating:

| Class | Elo Class                     | MMR Rating  |
| ---   | ---                           | ---         |
| 0     | Iron                          | 0 - 579     |
| 1     | Bronze                        | 579 - 1207  |
| 2     | Silver                        | 1207 - 1619 |
| 3     | Gold                          | 1619 - 1980 |
| 4     | Platinum                      | 1980 - 2329 |
| 5     | Diamond                       | 2329 - 2729 |
| 6     | Master/Grandmaster/Challenger | 2729 - 3386 |

The input to the model would consist of each player's data (there are 10 players in a match) at every 15 minutes. Each player would be represented as a vector of `[x, y, Gold, Exp, Dmg]` where: 
1. `x` represent the x position,
2. `y` represent the y position,
3. `Gold` represents the amount of the in-match currency,
4. `Exp` represents the amount of experience, and
5. `Dmg` represents the total amount of damage dealt to enemy players in one specific timeframe.

The dimension of each input unit is 5 $\times$ 10 = 50, and so the dimension of a single data point is (15, 50). On the other hand, the input label will be the class of the average ELO ratings of 10 players in a game represented in one-hot vector with size 7. 

Since we want to make predictions based on a sequence, we decided to use a LSTM architecture of the recurrent neural network with a maximum length of 15-time frames with each time frame taken at an interval of 1 minute. We will be using PyTorch's LSTM with 64 hidden units. At the end of the model of our network, we use a Multilayer Perceptron layer to output the probability distribution across 7 classes we defined above. We start with 15 fully connected layers. 

## Model

### Model Figure
<!-- A figure/diagram of the model architecture that demonstrates understanding of the steps involved in computing the forward pass. We are looking to see if you understand the steps involved in the model computation (i.e. are you treating the model as a black box or do you understand what it’s doing?) -->

![Alt text](/README_figures/model_figure.png?raw=true)

### Model Parameters
<!-- Count the number of parameters in the model, and a description of where the parameters come from. Again, we are looking to see if you understand what the model is doing, and what parameters are being tuned. -->
There are 15 input units in total. Then there are 15 hidden units corresponding to 15 input units. And we 
have 15 output units. Overall, there are 45 parameters in the model.


### Examples
<!-- Examples of how the model performs on two actual examples from the test set: one successful and one unsuccessful. -->


## Data

### Data Source
<!-- Describe the source of your data. -->
We retrieved the match data from the official League of Legends API allowed under www.riotgames.com/en/legal and the ELO ratings of all players from na.whatismymmr.com API allowed under Creative Commons Attribution 4.0 International License. The data retrieved is from the North America region.

### Data Summary
<!-- Provide summary statistics of your data to help interpret your results, similar to in the proposal. Please review the feedback provided in the proposal for some guidance on what information is helpful for interpreting your model behaviour.-->

We retrieved 10,000 datapoints from the sources, and only 8500 of them can be considered as valid inputs to the model. As you can see from the two histograms we constructed from the valid inputs, the data has a unimodal distribution, with Silver (class 2) as the most common ELO class, which follow the official rank distribution found at www.leagueofgraphs.com/rankings/rank-distribution/na. 

![Alt text](/README_figures/elo_histogram.png?raw=true)
![Alt text](/README_figures/mmr_histogram.png?raw=true)


### Data Transformation
<!-- Describe how you transformed the data, i.e. the steps you took to turn the data from what you downloaded, to something that a neural network can use as input. We are looking for a concise description that has just enough information for another person to replicate your process.-->

With the official API, we retrieved the match data and the players' ID in that match, then we use the players' ID to retrieve their MMR ratings from na.whatismymmr.com. The information retrieved is saved in a JSON file. From each of the JSON file we build, we extract `timeline` and `elo` to be our input and label data respectively. The array `timeline` consists of the 10 players data (as mentioned in the introduction) on each minute of the game appended together. The array `elo` contains 10 MMR ratings of each player in the game, so we take the average of the 10 values and classify it to one of the seven ELO classes we have based on index. The class 0-6 represented in one-hot vector is the label of the datapoint.

To make sure that all the input data have the same length, we only take the first 15 minutes of the game data and discharged any game that has less than 15 minutes in duration. We also discharged any datapoints that have incomplete values, for example: if the source cannot find the MMR rating of a specific player, we got `NULL` value.


### Data Split
<!-- If appropriate to your project, describe how the train/validation/test set was split. Note that splitting strategy is not always straightforward, so we are looking to see a split that can be justified. -->
| Dataset           | Distribution |
| ---               | ---          |
| Training Data     | 60%          |
| Validation Data   | 20%          |
| Test Data         | 20%          |

## Training Curve
<!--The training curve of your final model. We are looking for a curve that shows both training and validation performance (if applicable). Your training curve should look reasonable for the problem that you are solving.-->

## Hyperparameter Tuning
<!--A justification that your implemented method performed reasonably, given the difficulty of the problem—or a hypothesis for why it doesn’t. This is extremely important. We are looking for an interpretation of the result. You may want to refer to your data summary and hyperparameter choices to make your argument. -->

## Quantitative and Qualitative Results
<!-- Describe the quantitative and qualitative results. You may choose to use a table or figure to aid in your description. We are looking for both a clear presentation, and a result that makes sense given your data summary. (As an extreme example, you should not have a result that performs worse than a model that, say, predicts the most common class.)-->

### Quantitative Measures
<!-- A description and justification of the quantitative measure that you are using to evaluate your results. For some problems this will be straightforward. For others, please justify the measure that you chose. -->

## Justification of Results
<!-- A justification that your implemented method performed reasonably, given the difficulty of the problem—or a hypothesis for why it doesn’t. This is extremely important. We are looking for an interpretation of the result. You may want to refer to your data summary and hyperparameter choices to make your argument. -->

## Ethical Consideration
We believe that the RNN model we created can be used for both public and professional match evaluation. The evaluation can be done by comparing the ELO rating generated by our model to each player actual ELO rating. From the comparison, we can evaluate the match gameplay quality; whether the performance of **all the players** reflect the average level of ELO rating they are in right now.  

The prediction is generated by taking all of the 10 players in a match as an input; this means the value generated is a generalization of 10 players' performance which is not an accurate representation of individual performance. A player may have good individual performance in a match but the model says otherwise (by generating much lower ELO rating than the average of 10 players' ELO ratings), and vice versa.

An ethical problem will arise when our model is misused to evaluate individual performance, especially in professional scenes. The misinterpretation of the generated ELO rating can lead to cyberbullying targeted to specific professional players or teams. A player/team can be a target for cyberbullying because the model (indirectly) rated their latest match poorly by generating low ELO rating below what is expected from professional players. Therefore, we emphasize the model's purpose as a **match evaluation** tool and **not** an individual evaluation tool. 

## Authors

1005434558 - Josh Alexander (josh.alexander@mail.utoronto.ca)
- Put README.md together
- ..

1005426549 - Xinhao Hou (_@mail.utoronto.ca)
- Created the GitHub repository
- Wrote and run data collection script
- Wrote data processing script 
- ..

1004883860 - Zhixuan Yan (zhixuan.yan@mail.utoronto.ca)
- wrote README.md
- ..
