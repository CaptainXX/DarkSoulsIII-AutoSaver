
class QSS():
    def __init__(self):
        self.initQSS()

    # 美化：指 给组件加上QSS
    def initQSS(self):
        self.body = '''
        #body{
            background-color: #fff;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
        }
        '''

        self.btn = '''
        .QPushButton{
            background-color: #1B9AF7;
            border-color: #1B9AF7;
            border-radius: 4px;
            font-size: 16px;
            height: 30px;
            line-height: 30px;
            padding: 0 30px;
            margin: 0 30px 0 0;
            font-weight: 500;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            text-decoration: none;
            text-align: center;
            color: #FFF;
        }
        '''
        self.btn_Hover = '''
        .QPushButton{
            background-color: #229FFD;
            border-color: #1B9AF7;
            border-radius: 4px;
            font-size: 16px;
            height: 30px;
            line-height: 30px;
            padding: 0 30px;
            margin: 0 30px 0 0;
            font-weight: 500;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            text-decoration: none;
            text-align: center;
            color: #666;
        }
        '''
        self.btn_Press = '''
        .QPushButton{
            background-color: #2798eb;
            border-color: #2798eb;
            border-radius: 4px;
            font-size: 16px;
            height: 30px;
            line-height: 30px;
            padding: 0 30px;
            margin: 0 30px 0 0;
            font-weight: 500;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            text-decoration: none;
            text-align: center;
            color: #0880d7;
        }        
        '''
        self.btn_disabled = '''
        .QPushButton{
            background-color: #eee;
            border-color: #2798eb;
            border-radius: 4px;
            font-size: 16px;
            height: 30px;
            line-height: 30px;
            padding: 0 30px;
            margin: 0 30px 0 0;
            font-weight: 500;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            text-decoration: none;
            text-align: center;
            color: #333;
        }    
        '''


        self.label_h2 = '''
        .QLabel{
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            font-weight: 500;
            line-height: 1.1;
            color: inherit;
            font-size: 22px;
            padding: 50px 0 2px 0;
        }                
        '''
        self.label_h4 = '''
        .QLabel{
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            font-weight: 500;
            line-height: 1.1;
            color: inherit;
            font-size: 18px;
        }                
        '''
        self.label_h6 = '''
        .QLabel{
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            font-weight: 300;
            line-height: 1.1;
            color: inherit;
            font-size: 12px;
        }                
        '''
        self.label_h6_warning = '''
        .QLabel{
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            font-weight: 500;
            line-height: 1.1;
            color: #FF0000;
            font-size: 16px;
        }                
        '''

        self.input = '''
        .QLineEdit{
            height: 28px;
            padding: 6px 12px;
            font-size: 14px;
            line-height: 1.42857143;
            color: #555;
            background-color: #fff;
            background-image: none;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
        }
        '''
        self.input_focus = '''
        .QLineEdit{
            height: 28px;
            padding: 6px 12px;
            font-size: 14px;
            line-height: 1.42857143;
            color: #555;
            background-color: #ccc;
            background-image: none;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
        }
        '''

        self.input_box = '''
        
        '''

        self.comboBox = '''
        .QComboBox {
            padding: 5px;
            margin: 0;
            border: 1px solid #ccc;
            border-radius: 6px;    
            background-color: #fff;
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;        
        }
        QComboBox::drop-down {
            width: 25px;
            border-left-width: 3px;
            border-left-color: #ccc;
            border-left-style: solid;
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
            background:transparent;
        }
        QComboBox::down-arrow {
            image: url(:/images/arrow.png);
        }
        '''

        self.log_normal = '''
        <style type="text/css">
        p {
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            padding: 0;
            margin: 0;
            color: #000;
            font-weight: 490;
        }
        </style>
        '''
        self.log_good = '''
        <style type="text/css">
        p {
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            padding: 0;
            margin: 0;
            color: #00cc00;
            font-weight: 490;
        }
        </style>
        '''
        self.log_warning = '''
        <style type="text/css">
        p {
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            padding: 0;
            margin: 0;
            color: #aaaa00;
            font-weight: 490;
        }
        </style>
        '''
        self.log_error = '''
        <style type="text/css">
        p {
            font-family: "Microsoft YaHei UI", "Microsoft YaHei", serif, Times, TimesNR;
            padding: 0;
            margin: 0;
            color: #ff0000;
            font-weight: 490;
        }
        </style>
        '''


