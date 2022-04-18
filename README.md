# MMR Predictor

## Introduction
<!-- What deep learning model are you building? We are looking for a clear and concise description that uses standard deep learning terminology. Clearly describe the type of task that you are solving, and what your input/outputs are. -->

MMR Predictor is a recurrent neural network model that uses LSTM architecture to do a multi-class classification task. In this model, we introduce 7 classes of ELO rating:

| No  | Elo Class                     | MMR Rating  |
| --- | ---                           | ---         |
| 0   | Iron                          | 0 - 579     |
| 1   | Bronze                        | 579 - 1207  |
| 2   | Silver                        | 1207 - 1619 |
| 3   | Gold                          | 1619 - 1980 |
| 4   | Platinum                      | 1980 - 2329 |
| 5   | Diamond                       | 2329 - 2729 |
| 6   | Master/Grandmaster/Challenger | 2729 - 3386 |

The input to the model would consist of each player's data (there are 10 players in a match) at every 15 minutes. Each player would be represented as a vector of `[x, y, Gold, Exp, Dmg]` where: 
1. `x` represent the x position,
2. `y` represent the y position,
3. `Gold` represents the amount of the in-match currency,
4. `Exp` represents the amount of experience, and
5. `Dmg` represents the amount of damage dealt to enemy players in one specific timeframe.

The dimension of each input unit is 5 $\times$ 10 = 50, and so the dimension of a single data point is (15, 50). On the other hand, the input label will be the class of the average ELO ratings of 10 players in a game represented in one-hot vector with size 7. 

Since we want to make predictions based on a sequence, we decided to use a LSTM architecture of the recurrent neural network with a maximum length of 15-time frames with each time frame taken at an interval of 1 minute. We will be using PyTorch's LSTM with 64 hidden units. At the end of the model of our network, we use a Multilayer Perceptron layer to output the probability distribution across 7 classes we defined above. We start with 15 fully connected layers. 

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

prediction tensor([[2]], device='cuda:0')
target tensor([[2]], device='cuda:0')
prediction tensor([[2]], device='cuda:0')
target tensor([[5]], device='cuda:0')

Please see the jupyters notebook for for details  

## Data

### Data Summary
<!-- Provide summary statistics of your data to help interpret your results, similar to in the proposal. Please review the feedback provided in the proposal for some guidance on what information is helpful for interpreting your model behaviour.-->
![Alt text](/data_distribution.png?raw=true)
### Data Source
<!-- Describe the source of your data. -->
We retrieved the match data from the official League of Legends API allowed under www.riotgames.com/en/legal and the ELO ratings of all players from na.whatismymmr.com API allowed under Creative Commons Attribution 4.0 International License. 


### Data Transformation
<!-- Describe how you transformed the data, i.e. the steps you took to turn the data from what you downloaded, to something that a neural network can use as input. We are looking for a concise description that has just enough information for another person to replicate your process.-->

From each of the JSON file, we extract `timeline` and `elo` to be our input and label data respectively. The array `timeline` consists of the 10 players data (position, gold, experience, damage dealt) on each minute of the game appended together. The array `elo` contains 10 elo ratings of each player in the game. We take the average of the 10 values and classify it to one of the seven classes we have based on index (Iron, Bronze, Silver, Gold, Platinum, Diamond, Master/Grandmaster/Challenger). The class (0-6) is the label of the datapoint.


### Data Split
<!-- If appropriate to your project, describe how the train/validation/test set was split. Note that splitting strategy is not always straightforward, so we are looking to see a split that can be justified. -->
Training Data: 60%
Validation Data: 20%
Test Data:  20%
<!-- Missing justification -->

## Training Curve
<!--The training curve of your final model. We are looking for a curve that shows both training and validation performance (if applicable). Your training curve should look reasonable for the problem that you are solving.-->
![Alt text](/loss_accuracy_graph.png?raw=true)

## Hyperparameter Tuning
<!--A justification that your implemented method performed reasonably, given the difficulty of the problem—or a hypothesis for why it doesn’t. This is extremely important. We are looking for an interpretation of the result. You may want to refer to your data summary and hyperparameter choices to make your argument. -->

We used the intial training parameter of 64 hidden units a batch size of 64 and a learning rate of 0.07. We first tried tuning the number of hidden units since this should have the most effect on the model. We have tried values up to 126 hidden units and seen no significant improvement to our model. Than we tried tuning the learning rate. We increased the training rate from 0.07 to 0.1 and we found improvement in terms of training speed. The number of iterations where we reached final accuracy went from 50 to about 30 iterations. During the above tuning we also decided to lower our batch size from 64 to 32 to see better stability in the training and validation accuracy. Looking at the prediction vs the label we saw that out model is predicting the class 2 which is the mosty common class in our data. 
![Alt text](/training_accuracy.png?raw=true)

## Quantitative and Qualitative Results
<!-- Describe the quantitative and qualitative results. You may choose to use a table or figure to aid in your description. We are looking for both a clear presentation, and a result that makes sense given your data summary. (As an extreme example, you should not have a result that performs worse than a model that, say, predicts the most common class.)-->

Looking at the result we can see the model tries to predict the most common class in our training data. Which I think because the data we collected shows a normal distribution center at class 2 the model found it is better to use class 2 as a prediction. Maybe if the data is in an uniform distribution we would see better training results. Another reason that caused our model to predict the most common target in our training data is the lack of difference between the different classes. The data we collection on show statistics from minute to minute (limitation from the official Riot API) so the model would have diffculty spotting patterns in gameplay since our training data lacks detail. 

### Quantitative Measures
<!-- A description and justification of the quantitative measure that you are using to evaluate your results. For some problems this will be straightforward. For others, please justify the measure that you chose. -->
We don't think our model provides meanful results since the model is only outputing the most common target in our data. 


## Justification of Results
<!-- A justification that your implemented method performed reasonably, given the difficulty of the problem—or a hypothesis for why it doesn’t. This is extremely important. We are looking for an interpretation of the result. You may want to refer to your data summary and hyperparameter choices to make your argument. -->

Looking at the result I don't think our model performs well. I think this is because the lack of difference in training data between high vs low ranked players. Also our training data lacked detail since it is limited by the official Riot API and the model failed to distinguish between high ranked game play from low ranked gameplay. The training data for all ranks showed a similar trend therefore our model is unable to distinguish between high and low elo players. 

## Ethical Consideration
We believe that the RNN model we created can be used for both public and professional match evaluation. The evaluation can be done by comparing the ELO rating generated by our model (gELO) to each player actual ELO rating. From the comparison, we can evaluate the match gameplay quality; whether the performance of **all the players** reflect the level of ELO rating they are in right now.  

The gELO is generated by taking all of the 10 players in a match as an input; this means the value generated is a generalization of 10 players' performance which is not an accurate representation of individual performance. A player may have good individual performance in a match but the model says otherwise (by generating much lower ELO rating than the average of 10 players' ELO ratings), and vice versa.

An ethical problem will arise when our model is misused to evaluate individual performance, especially in professional scenes. The misinterpretation of the generated ELO rating can lead to cyberbullying targeted to specific professional players or teams. A player/team can be a target for cyberbullying because the model (indirectly) rated their latest match poorly by generating low ELO rating below what is expected from professional players. Therefore, we emphasize the model's purpose as a **match evaluation** tool and **not** an individual evaluation tool. 

## Authors

1005434558 - Josh Alexander (josh.alexander@mail.utoronto.ca)
- Put README.md together
- Fixed some issue with the data processing
- Ethical Consideration

1005426549 - Xinhao Hou (xinhao.hou@mail.utoronto.ca)
- Created the GitHub repository
- Wrote and run data collection script (DataCollection folder)
- Wrote data processing script 
- Hyperparameter Tuning

1004883860 - Zhixuan Yan (zhixuan.yan@mail.utoronto.ca)
- wrote README.md
- Model Figures
- Data processing 
