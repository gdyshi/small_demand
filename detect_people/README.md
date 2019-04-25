 ## 功能
 * 检测低分率图片中人的活动，将目标物体框出来
  
## 制作数据

训练新数据集也非常简单直接。只需将您的检测标签文件转换为以下格式：

```
/path/training/image_2/000000.png,712.40,143.00,810.73,307.92,Pedestrian
/path/training/image_2/000001.png,599.41,156.40,629.75,189.25,Truck
```
这是`/path/to/img.png，x1，y1，x2，y2，class_name`，有了这个简单的文件，我们不需要类映射文件，我们的训练程序会自动统计这个。
可用脚本`generate_anno_file.py 图片路径 标签路径`制作

## 训练
```
train_frcnn_kitti.py
```

## 预测
```
predict_kitti.py
```
预测图片放在 images 下，预测结果放在 result_images 下
