import pandas as pd
import matplotlib.pyplot as plt
question = str()
test = 'Монах выхватил посох и встал на пути нарушителя:– Зачем ты пришел к нам в монастырь? – спросил он.– Какое тебе дело, пшел вон с дороги! – огрызнулся чужак.'
for i in test:
    if '?' in i:
        question = question + ("?")
    elif '!' in i:
        question = question + ("!")
    elif '.' in i:
        question = question + (".")
    elif ":" in i:
        question = question + (":")
        
char_list = list(question)

df = pd.DataFrame({'chars': char_list})
df = df[df.chars != ' ']
df['num'] = 10
df = df.groupby('chars').sum().sort_values('num', ascending=False) / len(df)

plt.bar(df.index, df.num, width=0.5, color='g')
plt.show()
