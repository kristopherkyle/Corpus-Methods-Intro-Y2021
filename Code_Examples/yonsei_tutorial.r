install.packages("ggplot2")
install.packages("dplyr")
library(dplyr)
library(ggplot2)

mydata <- read.csv("nict_processed_wscore.txt", sep = "\t")
summary(mydata) #get basic descriptive statistics

#create scatterplots
#mattr
ggplot(mydata, aes(y = Score, x = mattr)) +
  #geom_point() + #this can also be used
  geom_jitter() + #geom_jitter makes it easier to see overlapping points
  geom_smooth(method = "lm")

#add others here
#av_freq


#pos_prop


#neg_prop



# Run correlations:
cor(mydata$mattr,mydata$Score) #0.4877

#add others here
#av_freq


#pos_prop


#neg_prop

corr_matrix <- cor(select(mydata,-filename,-nwords))
print(corr_matrix)

## Run a linear regression

model1 <- lm(Score~mattr,data = mydata)
summary(model1)

### Visualize the results
mydata$m1pred <- predict(model1) #add values predicted by the model to the dataframe

ggplot(mydata, aes(y = Score, x = m1pred)) +
  #geom_point() + #this can also be used
  geom_jitter() + #geom_jitter makes it easier to see overlapping points
  geom_smooth(method = "lm")

#add others here
#av_freq


#pos_prop


#neg_prop

## Run a multiple regression

multi_model <- lm(Score~mattr + av_freq + neg_prop,data = mydata)
summary(multi_model)

#visualize the results

mydata$multipred <- predict(multi_model) #add values predicted by the model to the dataframe

ggplot(mydata, aes(y = Score, x = multipred)) +
  #geom_point() + #this can also be used
  geom_jitter() + #geom_jitter makes it easier to see overlapping points
  geom_smooth(method = "lm")