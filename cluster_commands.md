# Εντολές για εκτέλεση σε cluster με 1,2,4 reducers

##### 1. Δημιουργία νέου καταλόγου `mkdir -p cluster`
##### 2. `cd cluster`
##### 3. **Μεταφέρω στον παραπάνω κατάλογο μέσω FileZilla τα 2 αρχεία .py**

<hr />

## Για τις δοκιμές (15 εκτελέσεις συνολικά)

### Ελέγχουμε αν βρισκόμαστε στον κατάλογο `cluster` εκτελώντας `pwd` => `/home/user/cluster`

### 5 εκτελέσεις με 1 Reducer Task

1. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \
      -numReduceTasks 1 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r1_1
2. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 1 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r1_2
3. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 1 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r1_3
4. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 1 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r1_4
5. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 1 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r1_5

### 5 εκτελέσεις με 2 Reducer Tasks

1. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 2 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r2_1
2. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 2 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r2_2
3. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 2 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r2_3
4. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 2 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r2_4
5. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 2 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r2_5
      
### 5 εκτελέσεις με 4 Reducer Tasks

1. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 4 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r4_1
2. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 4 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r4_2
3. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 4 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r4_3
4. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 4 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r4_4
5. ~/hadoop/bin/hadoop jar ~/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.1.jar -files mapper.py,reducer.py \ 
      -numReduceTasks 4 \
      -mapper mapper.py \
      -reducer reducer.py \
      -input logfiles \
      -output cluster_r4_5
      
<hr />
