




class CompanyName:
    
    #把公司的代码转变成中文输出
    def descarn_company(self, company):
        if company == 'huitongkuaidi':
            companyname = '百世汇通(百世快递）'
            return companyname
        elif company == 'auspost':
            companyname = '澳大利亚邮政'
            return companyname
        elif company == 'fengxingtianxia':
            companyname = '风行天下'
            return companyname
        elif company == 'yuantong':
            companyname = '圆通速递'
            return companyname
        elif company == '':
            companyname = ''
            return companyname

            

    # 解析中文输入，为公司代码
    def parse_com(self, com):
        if com == '百世快递' or '百世汇通':
            return 'huitongkuaidi'
        
            
    