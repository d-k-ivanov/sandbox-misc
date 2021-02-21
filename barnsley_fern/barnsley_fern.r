# Barnsley's Fern

# create function of the probability and the current point
fractal_fern2 <- function(x, p){
  if (p <= 0.01) {
    m <- matrix(c(0, 0, 0, .16), 2, 2)
    f <- c(0, 0)
  } else if (p <= 0.86) {
    m <- matrix(c(.85, -.04, .04, .85), 2, 2)
    f <- c(0, 1.6)
  } else if (p <= 0.93) {
    m <- matrix(c(.2, .23, -.26, .22), 2, 2)
    f <- c(0, 1.6)
  } else {
    m <- matrix(c(-.15, .26, .28, .24), 2, 2)
    f <- c(0, .44)
  }
  m %*% x + f
}

# how many reps determines how detailed the fern will be
reps <- 1000000

# create a vector with probability values, and a matrix to store coordinates
p <- runif(reps)

# initialise a point at the origin
coords <- c(0, 0)

# compute Fractal Coordinates
m <- Reduce(fractal_fern2, p, accumulate = T, init = coords)
m <- t(do.call(cbind, m))

# Create plot
plot(m, type = "p", cex = 0.1, col = "darkgreen",
     xlim = c(-3, 3), ylim = c(0, 10),
     xlab = NA, ylab = NA, axes = FALSE)
