import sqlite3
filename = "db.sqlite3"
db = None
cursor=None 


def db_start(func):
    def inner(*args,**kwargs):
        db_open()
        data = func(*args,**kwargs) 
        db_close()
        return data 
    return inner   

def db_open():
    global db, cursor
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("""PRAGMA foreign_keys=on""")

def db_close():
    db.commit()
    cursor.close()
    db.close()


        

@db_start  
def addMainCategory():
    main_category = [
        ('Laptops','laptops'),
        ('Personal Computers', 'personal-computer'), 
    ]

    main_cpu = [
        ('intel core i5', 6, 0, 3500, 12),
        ('intel core i7', 12, 0, 6500, 32),
        ('intel core i9', 18, 2, 12500, 64),
    ]

    main_gpu = [
        ('RTX 3060', 1777, 12, 3200),
        ('RTX 3090', 2333, 16, 5200),
        ('RTX 4090', 3255, 32, 5200),
    ]    

    main_ram = [
        ('kingston fury 32', 32, 3200),
        ('corsair 1.6', 16, 1800),
        ('samnsung 2133', 8, 3200),
    ]


    main_ssd = [
        ('samsung ssd 2tb', 2000, 500),
        ('gigabyte 1tb', 1000, 700),
        ('kingston', 4000, 900),
    ]

    main_characteristics = [
        (144,'1920-1080',4500,1,1,1,1),
        (144,'2560-1440',8000,3,3,3,3),
        (240,'2560-1440',7500,2,2,2,2)
    ]

    # main_product = [
    #     ()
    # ]

    cursor.executemany("""INSERT INTO main_category(name,slug) VALUES (?,?) """, main_category)
    cursor.executemany("""INSERT INTO main_cpu(cpu_name,cpu_core,cpu_video_core,cpu_frequency,streams) VALUES (?,?,?,?,?) """, main_cpu)
    cursor.executemany("""INSERT INTO main_gpu(gpu_name,gpu_core,gpu_memory,gpu_frequency) VALUES (?,?,?,?) """, main_gpu)
    cursor.executemany("""INSERT INTO main_ram(ram_name,ram_size,ram_frequency) VALUES (?,?,?) """, main_ram)
    cursor.executemany("""INSERT INTO main_ssd(ssd_name,ssd_size,ssd_speed) VALUES (?,?,?) """, main_ssd)
    cursor.executemany("""INSERT INTO main_characteristics(hz,resolution,weight,cpu_id,gpu_id,ram_id,ssd_id) VALUES (?,?,?,?,?,?,?) """, main_characteristics)
    # cursor.executemany("""INSERT INTO main_product(created, updated, id, name, slug, description, price, variable, discount, category_id, characteristics_id) VALUES (?,?,?,?,?,?,?,?,?,?,?) """, main_product)



addMainCategory()