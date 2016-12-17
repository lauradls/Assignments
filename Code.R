mydata=read.table("/Users/laura/Desktop/zionstock2.csv", header=TRUE, sep=",", dec=".")

summary(mydata)

myreg=lm(mydata$date~mydata$close)

library(stargazer)
stargazer(myreg,
          type = "text")

plot(jitter(mydata$close), main="ZION Closing Price (10yrs)", xlab="ZION Closing Stock Price", ylab="Date")
##Run Regression
myregline=lm(mydata$date~mydata$close)
##Plot Line on top of data
abline(myregline, col="red")

stargazer(mydata, type = "text", title="Descriptive statistics", digits=1, out="table1.txt", flip=FALSE)


#TABLE2-Predictive Distribution of Vector of Interest Gaussian i.i.d. Model



#TABLE3-Predictive Distribution of Vector of Interest t-GARCH Model

reps <- 10000
rbeta(1,1,1)
rchisq(1, df=4)
v <-rchisq(1, df=4)+4
v
mu <- 0.08
rt(1, df=v)
rnorm(1, 0.05, 0.2)
  x1 <- replicate(reps, rbeta, rchisq)
# replicate
