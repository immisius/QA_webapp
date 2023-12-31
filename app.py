import streamlit as st
from transformers import pipeline

model_name = "tsmatz/roberta_qa_japanese"
qa_pipeline = pipeline(
    "question-answering",
    model=model_name,
    tokenizer=model_name)


st.write("# 日本語QAモデルのデモ")
st.write("## モデルの説明")
st.write("日本語のQAモデルです。")
st.write("モデルの詳細は[こちら](https://huggingface.co/tsmatz/roberta_qa_japanese)をご覧ください。")
st.write("## デモ")

init_context = '''2021年F1最終戦は劇的な展開を見せ、最終的にフェルスタッペンが逆転でワールドチャンピオンを獲得しました。フェルスタッペンはソフトタイヤでポールポジションからスタートしましたが、ハミルトンに先行を許す展開となりました。その後1周目のターン6でフェルスタッペンのアタックにより、ハミルトンはコーナーをカット、差を拡大しました。

フェルスタッペンの押し出しとハミルトンのショートカットについて審議が行われましたが、結果としてはどちらも問題なしとされ、ハミルトンが有利な立場を保つ形となりました。フェルスタッペンは13周目にハードタイヤへ変更。ハミルトンもすぐにピットインし、セルジオ・ペレスが一時的にトップを走行しました。

ペレスの走行によりフェルスタッペンとハミルトンとのギャップは一時的に縮まりましたが、ハミルトンのペースは依然として高く、フェルスタッペンの追撃は難航しました。終盤に向け、アルファロメオのアントニオ・ジョヴィナッツィが35周目にマシンを止め、バーチャルセーフティカーが導入されました。これに対応するため、フェルスタッペンは再び新品のハードタイヤに交換しました。

そしてレースは残り8周で大きく動きました。ウィリアムズのニコラス・ラティフィがクラッシュし、セーフティカーが導入されました。これに対してフェルスタッぺンはソフトタイヤに交換し、ハミルトンはピットインせずにトップの座を守りました。レースは残り1周で再スタートされ、新しいソフトタイヤを履いたフェルスタッペンは5コーナーでハミルトンを追い越し、逆転優勝を飾りました。

2021年のF1シーズンはフェルスタッぺンのワールドチャンピオン獲得、メルセデスのコンストラクターズチャンピオンとして終了しました。ただし、1周目の接触事故やセーフティカーの導入については、その後も議論が続くと予想されます。"
'''
context = st.text_area("文章を入力してください。", value=init_context, height=100)

init_question = "フェルスタッペンは何周目にハードタイヤに交換した？"

question = st.text_input("質問を入力してください。", value=init_question)

if st.button("質問に答える"):
    answer = qa_pipeline(question=question, context=context)
    st.write("回答: ")
    st.write(answer["answer"])
