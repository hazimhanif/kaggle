id <- as.integer(c(0:999999))

# ratio from weka using test set
#of <- as.integer(sample(c(0, 1), size = 1000000, replace = TRUE, prob = c(0.499226,0.500774)))

# ratio from kaggle submission 0-1 (original, 0=0.50050, 1=0.49950)
of <- as.integer(sample(c(0, 1), size = 1000000, replace = TRUE, prob = c(0.60050,0.39950)))


output <- cbind(id,of)
output <- data.frame(output)
colnames(output) <- c("id","label")
write.csv(output,file="D:/overfit.csv",row.names = FALSE)
