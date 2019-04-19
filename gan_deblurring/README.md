
# 数据准备

```
images/train/A   模糊后的训练数据
images/train/B   原始训练数据
images/test/A   模糊后的测试数据
images/test/B   原始测试数据
```

# 训练
```
train.py --n_images=2000 --batch_size=16 --log_dir log/dir --epoch_num=2000
```
训练后权重文件放在 weights 中

# 测试
```
test.py
```
生成的图片放在 result 中
