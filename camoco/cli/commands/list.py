import camoco as co

def list_command(args):
    if args.type != None and args.name != None:
        if args.terms:
            if args.type == 'GWAS':
                gwas = co.GWAS(args.name)
                print('\n'.join([x.id for x in gwas.iter_terms()]))
            elif args.type =='GOnt':
                gont = co.GOnt(args.name)
                print('\n'.join([x.id for x in gont.iter_terms()]))
        else:
            print(co.available_datasets(args.type,args.name))
    elif args.type != None and args.name == None:
        args.name = '%'
        print(co.available_datasets(args.type,args.name).to_string())
    else:
        args.type = '%'
        args.name = '%'
        print(co.available_datasets(args.type,args.name).to_string())
