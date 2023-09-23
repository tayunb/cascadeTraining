opencv_traincascade -data cascade_files -vec pos.vec -bg bg.txt \
-numPos 2700 -numNeg 1400 -numStages 20 -w 60 -h 60 -minHitRate 0.999 \
-maxFalseAlarmRate 0.5 -acceptanceRatioBreakVAlue 10e-5 -numThreads 2