# MMR Predictor

## Introduction
<!-- What deep learning model are you building? We are looking for a clear and concise description that uses standard deep learning terminology. Clearly describe the type of task that you are solving, and what your input/outputs are. -->

MMR Predictor is a < .. > that does multi-class classification.

Input data point description:
    Every data point would consist of each player’s position at every 15 minutes and the character that 
    the player is using. So each player would be represented as a vector of [gold, exp, damage, x, y]
    where gold will be the player gold at that time, exp represents the player experience at that time,
    damage represents the player damage to the enemy at that time, the character id would represent the 
    game character that the player chose, and x, y would be the positional data. And there are 10 players 
    per game in total. Therefore, the dimension of each input unit is 5*10=50. And the dimension of a 
    single data point is (15,50).

model design description:
    Since we want to make predictions about a sequence, we decided to use a LSTM architecture of the 
    recurrent neural network with a maximum length of 15-time frames with each time frame taken at an 
    interval of 1 minute. We choose to use 64 hidden units. And we apply LSTM from pytorch. At the end of 
    the model of our network, we would use an MLP layer to estimate the average MMR of the match. We 
    start with 15 fully connected layers. 

Output data point description:
    Our target would be a one hot vector with dimension of 7 representing the average ELO rating of all 
    players in a game. Our model would adjust its output to this target match’s average ELO. According to 
    the matchmaking system of the game League of Legends, there are 6 divisions with 4 tiers and 3 
    divisions with 1 tier with every tier representing a range of the ELO rating such as 1200-1270, 
    1270-1330 etc. Therefore, there are 27 tires in total. Thus, we would consider the prediction as a 
    correct prediction if it is in the target ELO range. 


## Model

### Model Figure
<!-- A figure/diagram of the model architecture that demonstrates understanding of the steps involved in computing the forward pass. We are looking to see if you understand the steps involved in the model computation (i.e. are you treating the model as a black box or do you understand what it’s doing?) -->

![Alt text](/image_figure.png?raw=true)

### Model Parameters
<!-- Count the number of parameters in the model, and a description of where the parameters come from. Again, we are looking to see if you understand what the model is doing, and what parameters are being tuned. -->
There are 15 input units in total. Then there are 15 hidden units corresponding to 15 input units. And we 
have 15 output units. Overall, there are 45 parameters in the model.


### Examples
<!-- Examples of how the model performs on two actual examples from the test set: one successful and one unsuccessful. -->


## Data

### Data Summary
<!-- Provide summary statistics of your data to help interpret your results, similar to in the proposal. Please review the feedback provided in the proposal for some guidance on what information is helpful for interpreting your model behaviour.-->

### Data Source
<!-- Describe the source of your data. -->
We retrieved the match data from the official League of Legends API allowed under www.riotgames.com/en/legal and the ELO ratings of all players from na.whatismymmr.com API allowed under Creative Commons Attribution 4.0 International License. 


### Data Transformation
<!-- Describe how you transformed the data, i.e. the steps you took to turn the data from what you downloaded, to something that a neural network can use as input. We are looking for a concise description that has just enough information for another person to replicate your process.-->

( Need description from the data collection script !! )

From each of the JSON file, we extract `timeline` and `elo` to be our input and label data respectively. The array `timeline` consists of the 10 players data (position, gold, experience, damage dealt) on each minute of the game appended together. The array `elo` contains 10 elo ratings of each player in the game. We take the average of the 10 values and classify it to one of the seven classes we have based on index (Iron, Bronze, Silver, Gold, Platinum, Diamond, Master/Grandmaster/Challenger). The class (0-6) is the label of the datapoint.


### Data Split
<!-- If appropriate to your project, describe how the train/validation/test set was split. Note that splitting strategy is not always straightforward, so we are looking to see a split that can be justified. -->
Training Data: 60%
Validation Data: 20%
Test Data:  20%
<!-- Missing justification -->

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
We believe that the RNN model we created can be used for both public and professional match evaluation. The evaluation can be done by comparing the ELO rating generated by our model (gELO) to each player actual ELO rating. From the comparison, we can evaluate the match gameplay quality; whether the performance of **all the players** reflect the level of ELO rating they are in right now.  

The gELO is generated by taking all of the 10 players in a match as an input; this means the value generated is a generalization of 10 players' performance which is not an accurate representation of individual performance. A player may have good individual performance in a match but the model says otherwise (by generating much lower ELO rating than the average of 10 players' ELO ratings), and vice versa.

An ethical problem will arise when our model is misused to evaluate individual performance, especially in professional scenes. The misinterpretation of the generated ELO rating can lead to cyberbullying targeted to specific professional players or teams. A player/team can be a target for cyberbullying because the model (indirectly) rated their latest match poorly by generating low ELO rating below what is expected from professional players. Therefore, we emphasize the model's purpose as a **match evaluation** tool and **not** an individual evaluation tool. 

## Authors

1005434558 - Josh Alexander (josh.alexander@mail.utoronto.ca)
- Put README.md together
- ..

1005426549 - Xinhao Hou (_@mail.utoronto.ca)
- Created the GitHub repository
- Wrote and run data collection script <!-- may be better if this replaced by the actual filename -->
- Wrote data processing script 
- ..

1004883860 - Zhixuan Yan (zhixuan.yan@mail.utoronto.ca)
- wrote README.md
- ..
