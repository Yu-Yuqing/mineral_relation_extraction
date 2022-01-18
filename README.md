# relation-extraction
中文关系抽取



### bert_model
从 https://huggingface.co/models 下载bert-base-chinese模型，解压在pretrained_models下

bert-base-chinese目录结构如下：
```
bert-base-chinese/
├── config.json
├── pytorch_model.bin
└── vocab.txt 
```

### 模型训练20轮的评测结果：

run the train.py
```
              precision    recall  f1-score   support

          年代     0.9907    0.9876    0.9891       323
          包含     0.9925    1.0000    0.9963       133
          类型     0.9976    0.9927    0.9951       826
          方位     0.9756    0.9816    0.9786       163
          发育     0.9784    0.9875    0.9829       321

    accuracy                         0.9904      1766
   macro avg     0.9870    0.9899    0.9884      1766
weighted avg     0.9904    0.9904    0.9904      1766

```

### 模型预测效果：

run the demo_predict.py



参考：

https://github.com/Jacen789/relation-extraction

https://github.com/thunlp/OpenNRE

https://github.com/monologg/R-BERT

https://github.com/crownpku/Information-Extraction-Chinese

# mineral_relation_extraction
# mineral_relation_extraction
# mineral_relation_extraction
# mineral_relation_extraction
# mineral_relation_extraction
# mineral_relation_extraction
