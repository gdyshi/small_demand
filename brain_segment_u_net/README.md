
 ## 功能
 * 
  
## 填充数据

训练新数据集也非常简单直接。只需将您的检测标签文件转换为以下格式：

```
/path/training/image_2/000000.png,712.40,143.00,810.73,307.92,Pedestrian
/path/training/image_2/000001.png,599.41,156.40,629.75,189.25,Truck
```
训练图片`data/brain/train/image`
训练标签`data/brain/train/label`
测试图片`data/brain/test/image`

## 训练
```
main.py
```

## 测试
```
test.py
```
测试结果放在 `data/brain/test/pred` 下
