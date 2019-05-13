
 ## 功能
 * 卫星图片车辆识别
  
## 填充数据

将训练图片数据放在 `data\car\train\JPEGImages`文件夹内
将训练图片标注放在 `data\car\train\Annotations`文件夹内
将验证图片数据放在 `data\car\valid\JPEGImages`文件夹内
将验证图片标注放在 `data\car\valid\Annotations`文件夹内

## 训练
```
python3 train.py -c config.json
```

## 测试
待测试的数据放在`images`下
```
python3.5 predict.py -c config.json -w full_yolo_kangaroo.h5 -i images
```
预测结果放在 `images` 下， 文件名以_detected结尾
