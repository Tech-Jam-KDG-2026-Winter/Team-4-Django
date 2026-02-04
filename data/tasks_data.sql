-- Drift Jellyfish タスクデータ
-- レベル1〜50、各レベル3タスク、各タスク3つのYES/NO質問

-- ====================
-- レベル1〜7: 自分の部屋で、一人で
-- ====================

-- レベル1
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(1, 'alone', 'カーテンを開ける', 'ゆっくりでいい。光を感じよう', '["カーテンを開けられましたか？", "光を感じることができましたか？", "部屋が明るくなったと感じましたか？"]', datetime('now')),
(1, 'alone', '窓を開けて深呼吸する', '外の空気を感じてみよう', '["窓を開けられましたか？", "深呼吸できましたか？", "外の空気を感じられましたか？"]', datetime('now')),
(1, 'alone', 'ベッドから起き上がる', '今日も、君のペースで行こう', '["ベッドから起き上がれましたか？", "体を動かせましたか？", "少しすっきりしましたか？"]', datetime('now'));

-- レベル2
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(2, 'alone', 'コップ一杯の水を飲む', 'ゆっくりでいい。体に水分を', '["水を飲めましたか？", "喉の渇きを感じましたか？", "体が潤った感じがしましたか？"]', datetime('now')),
(2, 'alone', '顔を洗う', '冷たい水で、目を覚まそう', '["顔を洗えましたか？", "水の冷たさを感じましたか？", "少し目が覚めましたか？"]', datetime('now')),
(2, 'alone', '着替える', '新しい服で、新しい気持ちに', '["着替えられましたか？", "服を選べましたか？", "気分が少し変わりましたか？"]', datetime('now'));

-- レベル3
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(3, 'alone', 'ベッドを整える', '小さなことから、少しずつ', '["ベッドを整えられましたか？", "部屋が少し片付きましたか？", "達成感を感じましたか？"]', datetime('now')),
(3, 'alone', '部屋の換気をする', '新しい空気を部屋に入れよう', '["換気できましたか？", "5分以上窓を開けられましたか？", "部屋の空気が変わったと感じましたか？"]', datetime('now')),
(3, 'alone', '好きな音楽を1曲聴く', '心が少し軽くなるかも', '["音楽を聴けましたか？", "好きな曲を選べましたか？", "少し気分が良くなりましたか？"]', datetime('now'));

-- レベル4
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(4, 'alone', '鏡で自分の顔を見る', 'ありのままの君でいい', '["鏡を見られましたか？", "自分の顔を見つめられましたか？", "少し落ち着きましたか？"]', datetime('now')),
(4, 'alone', '部屋で軽くストレッチ', '体をほぐしてみよう', '["ストレッチできましたか？", "体を動かせましたか？", "少し体がほぐれましたか？"]', datetime('now')),
(4, 'alone', '机の上を少し片付ける', '見える範囲だけでいい', '["片付けられましたか？", "何か捨てられましたか？", "机がすっきりしましたか？"]', datetime('now'));

-- レベル5
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(5, 'alone', '朝ごはんを食べる', '何でもいい、口にしてみよう', '["何か食べられましたか？", "朝食を用意できましたか？", "少しお腹が満たされましたか？"]', datetime('now')),
(5, 'alone', 'スマホを10分置いてみる', 'デジタルから少し離れよう', '["スマホを置けましたか？", "10分我慢できましたか？", "少し落ち着きましたか？"]', datetime('now')),
(5, 'alone', '今日の予定を1つ書き出す', '小さな計画を立ててみよう', '["予定を書けましたか？", "実現可能な予定でしたか？", "計画を立てられましたか？"]', datetime('now'));

-- レベル6
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(6, 'alone', '好きな本を1ページ読む', '1ページだけでも十分', '["本を開けましたか？", "1ページ読めましたか？", "内容が少し頭に入りましたか？"]', datetime('now')),
(6, 'alone', '部屋の電気を全部つける', '明るい部屋で過ごしてみよう', '["電気をつけられましたか？", "部屋が明るくなりましたか？", "気分が少し変わりましたか？"]', datetime('now')),
(6, 'alone', '深呼吸を5回する', 'ゆっくり、吸って、吐いて', '["深呼吸できましたか？", "5回続けられましたか？", "少し落ち着きましたか？"]', datetime('now'));

-- レベル7
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(7, 'alone', '今日の目標を1つ決める', '小さな目標でいい', '["目標を決められましたか？", "達成できそうな目標でしたか？", "やる気が少し出ましたか？"]', datetime('now')),
(7, 'alone', '自分の部屋から出る準備をする', '外に出る準備、できるかな', '["準備を始められましたか？", "靴を履けそうですか？", "少し勇気が出ましたか？"]', datetime('now')),
(7, 'alone', '昨日の自分を褒める', '昨日も頑張ったね', '["昨日を振り返れましたか？", "自分を褒められましたか？", "少し前向きになれましたか？"]', datetime('now'));

-- ====================
-- レベル8〜14: 家の中で、家族と
-- ====================

-- レベル8
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(8, 'family', '自分の部屋から出る', '廊下まで、行ってみよう', '["部屋から出られましたか？", "廊下に立てましたか？", "少し外の空気を感じましたか？"]', datetime('now')),
(8, 'family', '家族の気配を感じる', '誰かいる、それだけでいい', '["家族の存在を感じましたか？", "声や音が聞こえましたか？", "少し安心しましたか？"]', datetime('now')),
(8, 'family', 'リビングのドアを開ける', 'ドアを開けるだけでいい', '["ドアを開けられましたか？", "リビングを見られましたか？", "少し勇気が出ましたか？"]', datetime('now'));

-- レベル9
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(9, 'family', '家族におはようと言う', '小さな声でもいい', '["おはようと言えましたか？", "家族に聞こえましたか？", "反応がありましたか？"]', datetime('now')),
(9, 'family', 'リビングに5分いる', '同じ空間にいるだけでいい', '["リビングに入れましたか？", "5分いられましたか？", "家族と同じ空間にいられましたか？"]', datetime('now')),
(9, 'family', 'キッチンに行く', '何か飲み物を取りに行こう', '["キッチンに行けましたか？", "何か取れましたか？", "家族と会いましたか？"]', datetime('now'));

-- レベル10
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(10, 'family', '家族と同じ空間で過ごす', '会話しなくてもいい', '["同じ空間にいられましたか？", "10分以上いられましたか？", "落ち着いて過ごせましたか？"]', datetime('now')),
(10, 'family', '家族の顔を見る', '目を合わせなくてもいい', '["家族の顔を見られましたか？", "表情を確認できましたか？", "少し距離が縮まりましたか？"]', datetime('now')),
(10, 'family', 'ありがとうを1回言う', '小さなことでもいい', '["ありがとうと言えましたか？", "家族に伝わりましたか？", "言えて良かったと思いましたか？"]', datetime('now'));

-- レベル11
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(11, 'family', '家族と一緒に食事をする', '同じテーブルで食べてみよう', '["一緒に食事できましたか？", "同じテーブルに座れましたか？", "少し会話できましたか？"]', datetime('now')),
(11, 'family', '家族に1つ質問する', '天気のことでもいい', '["質問できましたか？", "家族は答えてくれましたか？", "会話が続きましたか？"]', datetime('now')),
(11, 'family', '家族の話を聞く', 'うなずくだけでもいい', '["話を聞けましたか？", "相槌を打てましたか？", "内容が理解できましたか？"]', datetime('now'));

-- レベル12
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(12, 'family', '家族と10分会話する', 'どんな話題でもいい', '["会話できましたか？", "10分続きましたか？", "楽しいと感じる瞬間がありましたか？"]', datetime('now')),
(12, 'family', '家族の手伝いをする', '簡単なことでいい', '["手伝えましたか？", "家族は喜んでくれましたか？", "役に立てたと感じましたか？"]', datetime('now')),
(12, 'family', 'テレビを家族と見る', '一緒にいる時間を過ごそう', '["一緒に見られましたか？", "同じ番組を見られましたか？", "少し楽しめましたか？"]', datetime('now'));

-- レベル13
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(13, 'family', '家族に「おやすみ」と言う', '1日の終わりに', '["おやすみと言えましたか？", "家族に伝わりましたか？", "穏やかに終われましたか？"]', datetime('now')),
(13, 'family', '家族と笑う', '笑顔になれる瞬間を', '["笑えましたか？", "家族も笑っていましたか？", "楽しい時間でしたか？"]', datetime('now')),
(13, 'family', '家族に今日あったことを話す', '小さなことでもいい', '["話せましたか？", "家族は聞いてくれましたか？", "話して良かったと思いましたか？"]', datetime('now'));

-- レベル14
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(14, 'family', '家族と一緒に料理する', '簡単な手伝いでもいい', '["料理に参加できましたか？", "何か作れましたか？", "家族と協力できましたか？"]', datetime('now')),
(14, 'family', '家族に悩みを1つ話す', '小さな悩みでもいい', '["悩みを話せましたか？", "家族は聞いてくれましたか？", "少し楽になりましたか？"]', datetime('now')),
(14, 'family', '家族と将来の話をする', 'ぼんやりした話でもいい', '["将来の話ができましたか？", "自分の考えを伝えられましたか？", "前向きな気持ちになれましたか？"]', datetime('now'));

-- ====================
-- レベル15〜21: 家の外へ
-- ====================

-- レベル15
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(15, 'outside', '玄関まで行く', 'ドアの前まで、行ってみよう', '["玄関まで行けましたか？", "ドアに触れられましたか？", "外を意識できましたか？"]', datetime('now')),
(15, 'outside', '玄関のドアを開ける', '開けるだけでいい', '["ドアを開けられましたか？", "外の空気を感じましたか？", "少し勇気が出ましたか？"]', datetime('now')),
(15, 'outside', '外の音を聞く', '耳を澄ませてみよう', '["外の音が聞こえましたか？", "何の音か分かりましたか？", "外の世界を感じられましたか？"]', datetime('now'));

-- レベル16
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(16, 'outside', '玄関の外に立つ', '1分だけでもいい', '["外に立てましたか？", "1分いられましたか？", "周りを見られましたか？"]', datetime('now')),
(16, 'outside', '靴を履いて外に出る', '一歩、外へ', '["靴を履けましたか？", "外に出られましたか？", "少し達成感がありましたか？"]', datetime('now')),
(16, 'outside', 'ポストを見に行く', '家のすぐ近くでいい', '["ポストまで行けましたか？", "郵便物を確認できましたか？", "戻ってこられましたか？"]', datetime('now'));

-- レベル17
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(17, 'outside', '家の前を往復する', '短い距離でいい', '["往復できましたか？", "5分以上外にいられましたか？", "少し慣れてきましたか？"]', datetime('now')),
(17, 'outside', '近所の景色を見る', '何か1つ、覚えておこう', '["景色を見られましたか？", "何か印象に残りましたか？", "外の世界を感じられましたか？"]', datetime('now')),
(17, 'outside', '外で深呼吸する', '外の空気を胸いっぱいに', '["外で深呼吸できましたか？", "空気の違いを感じましたか？", "少しリフレッシュできましたか？"]', datetime('now'));

-- レベル18
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(18, 'outside', '家の周りを一周する', 'ゆっくりでいい', '["一周できましたか？", "10分以上歩けましたか？", "疲れすぎませんでしたか？"]', datetime('now')),
(18, 'outside', '近所のコンビニまで歩く', '行くだけでもいい', '["コンビニまで行けましたか？", "道を覚えていましたか？", "無事に帰れましたか？"]', datetime('now')),
(18, 'outside', '外で5分立ち止まる', '周りを観察してみよう', '["立ち止まれましたか？", "周りを見られましたか？", "何か発見がありましたか？"]', datetime('now'));

-- レベル19
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(19, 'outside', 'コンビニで何か買う', '小さなものでいい', '["コンビニに入れましたか？", "何か買えましたか？", "店員さんと接せましたか？"]', datetime('now')),
(19, 'outside', '外で10分過ごす', 'どこでもいい、外にいよう', '["10分外にいられましたか？", "落ち着いて過ごせましたか？", "帰りたくなりませんでしたか？"]', datetime('now')),
(19, 'outside', '近所を散歩する', '目的地なしでいい', '["散歩できましたか？", "15分以上歩けましたか？", "楽しめましたか？"]', datetime('now'));

-- レベル20
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(20, 'outside', '公園まで行く', 'ベンチに座ってみよう', '["公園まで行けましたか？", "ベンチに座れましたか？", "少し休めましたか？"]', datetime('now')),
(20, 'outside', '外で20分過ごす', '慣れてきたね', '["20分外にいられましたか？", "焦らずいられましたか？", "外が怖くなくなってきましたか？"]', datetime('now')),
(20, 'outside', '知らない道を歩く', '新しい発見があるかも', '["新しい道を歩けましたか？", "迷わず帰れましたか？", "冒険できましたか？"]', datetime('now'));

-- レベル21
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(21, 'outside', '好きな場所を見つける', '外で落ち着ける場所', '["場所を見つけられましたか？", "そこで過ごせましたか？", "また行きたいと思いましたか？"]', datetime('now')),
(21, 'outside', 'その場所に30分いる', 'ゆっくり過ごそう', '["30分いられましたか？", "リラックスできましたか？", "時間が早く感じましたか？"]', datetime('now')),
(21, 'outside', '外で写真を1枚撮る', '記念に残そう', '["写真を撮れましたか？", "何を撮りましたか？", "良い思い出になりましたか？"]', datetime('now'));

-- ====================
-- レベル22〜28: 外で過ごす
-- ====================

-- レベル22
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(22, 'stay_outside', '図書館に入る', '静かな場所で過ごそう', '["図書館に入れましたか？", "中で過ごせましたか？", "落ち着いていられましたか？"]', datetime('now')),
(22, 'stay_outside', '外で1時間過ごす', '長い時間、外にいてみよう', '["1時間外にいられましたか？", "疲れすぎませんでしたか？", "充実していましたか？"]', datetime('now')),
(22, 'stay_outside', 'カフェに入る', '中を見るだけでもいい', '["カフェに入れましたか？", "中の様子を見られましたか？", "次も来たいと思いましたか？"]', datetime('now'));

-- レベル23
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(23, 'stay_outside', 'カフェで何か注文する', '飲み物1つでいい', '["注文できましたか？", "店員さんと話せましたか？", "ゆっくり飲めましたか？"]', datetime('now')),
(23, 'stay_outside', '外で本を読む', '公園やカフェで', '["外で本を読めましたか？", "集中できましたか？", "リラックスできましたか？"]', datetime('now')),
(23, 'stay_outside', '外で音楽を聴く', 'イヤホンで自分の世界を', '["音楽を聴けましたか？", "外の景色と音楽が合いましたか？", "気分が良くなりましたか？"]', datetime('now'));

-- レベル24
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(24, 'stay_outside', '外で2時間過ごす', '長く外にいられるように', '["2時間外にいられましたか？", "何をして過ごしましたか？", "時間が早く感じましたか？"]', datetime('now')),
(24, 'stay_outside', 'ショッピングモールに行く', '見て回るだけでもいい', '["モールに入れましたか？", "店を見て回れましたか？", "人混みは大丈夫でしたか？"]', datetime('now')),
(24, 'stay_outside', '外で昼食を食べる', 'レストランやカフェで', '["外で食事できましたか？", "ゆっくり食べられましたか？", "美味しかったですか？"]', datetime('now'));

-- レベル25
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(25, 'stay_outside', '映画館に行く', '映画を見なくてもいい、場所に慣れよう', '["映画館に行けましたか？", "中に入れましたか？", "雰囲気を楽しめましたか？"]', datetime('now')),
(25, 'stay_outside', '外で3時間過ごす', 'もう外も怖くないね', '["3時間外にいられましたか？", "いろんな場所に行けましたか？", "充実していましたか？"]', datetime('now')),
(25, 'stay_outside', '新しいお店を開拓する', '行ったことない場所へ', '["新しいお店に行けましたか？", "中に入れましたか？", "また行きたいと思いましたか？"]', datetime('now'));

-- レベル26
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(26, 'stay_outside', '外で半日過ごす', '朝から昼まで、または昼から夜まで', '["半日外にいられましたか？", "いろんなことができましたか？", "疲れすぎませんでしたか？"]', datetime('now')),
(26, 'stay_outside', '博物館や美術館に行く', '文化に触れてみよう', '["博物館に行けましたか？", "展示を見られましたか？", "何か印象に残りましたか？"]', datetime('now')),
(26, 'stay_outside', '外でスケッチする', '風景や物を描いてみよう', '["スケッチできましたか？", "集中できましたか？", "満足できる絵になりましたか？"]', datetime('now'));

-- レベル27
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(27, 'stay_outside', '電車やバスに乗る', '少し遠くへ行ってみよう', '["乗れましたか？", "目的地に着けましたか？", "問題なく過ごせましたか？"]', datetime('now')),
(27, 'stay_outside', '知らない街を歩く', '探検してみよう', '["知らない街に行けましたか？", "歩き回れましたか？", "楽しめましたか？"]', datetime('now')),
(27, 'stay_outside', '外で夕日を見る', '1日の終わりを感じよう', '["夕日を見られましたか？", "きれいだと感じましたか？", "穏やかな気持ちになれましたか？"]', datetime('now'));

-- レベル28
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(28, 'stay_outside', '1日中外で過ごす', '朝から夜まで', '["1日外にいられましたか？", "充実していましたか？", "家に帰りたいと思いましたか？"]', datetime('now')),
(28, 'stay_outside', '外で誰かを待つ', '待ち合わせの練習', '["待てましたか？", "落ち着いて待てましたか？", "時間を潰せましたか？"]', datetime('now')),
(28, 'stay_outside', '夜の外出をする', '夜の街を歩いてみよう', '["夜に外出できましたか？", "怖くなかったですか？", "夜の雰囲気を楽しめましたか？"]', datetime('now'));

-- ====================
-- レベル29〜35: 人と関わる
-- ====================

-- レベル29
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(29, 'interact', '店員さんに「ありがとう」と言う', '小さな声でもいい', '["ありがとうと言えましたか？", "店員さんに聞こえましたか？", "言えて良かったと思いましたか？"]', datetime('now')),
(29, 'interact', '誰かに挨拶する', 'すれ違う人でもいい', '["挨拶できましたか？", "相手は返してくれましたか？", "勇気が出ましたか？"]', datetime('now')),
(29, 'interact', '店員さんと目を合わせる', '一瞬でもいい', '["目を合わせられましたか？", "笑顔を見られましたか？", "少し緊張しましたか？"]', datetime('now'));

-- レベル30
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(30, 'interact', '店員さんに質問する', '商品の場所を聞いてみよう', '["質問できましたか？", "答えてもらえましたか？", "目的の物を見つけられましたか？"]', datetime('now')),
(30, 'interact', '知らない人に道を聞く', '話しかける練習', '["道を聞けましたか？", "相手は教えてくれましたか？", "目的地に着けましたか？"]', datetime('now')),
(30, 'interact', 'レジで会話する', '天気の話でもいい', '["会話できましたか？", "店員さんは反応してくれましたか？", "楽しかったですか？"]', datetime('now'));

-- レベル31
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(31, 'interact', '誰かと5分会話する', '家族以外の人と', '["会話できましたか？", "5分続きましたか？", "楽しめましたか？"]', datetime('now')),
(31, 'interact', '図書館で本を借りる', 'カウンターで手続き', '["カウンターに行けましたか？", "本を借りられましたか？", "スムーズにできましたか？"]', datetime('now')),
(31, 'interact', '誰かに笑顔を向ける', '自然な笑顔を', '["笑顔を向けられましたか？", "相手も笑ってくれましたか？", "温かい気持ちになれましたか？"]', datetime('now'));

-- レベル32
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(32, 'interact', '誰かと10分会話する', '少し長く話してみよう', '["10分会話できましたか？", "話題が続きましたか？", "楽しいと感じましたか？"]', datetime('now')),
(32, 'interact', '美容院や床屋に行く', '人と接する時間', '["行けましたか？", "会話できましたか？", "リラックスできましたか？"]', datetime('now')),
(32, 'interact', '誰かに自分から話しかける', '勇気を出して', '["話しかけられましたか？", "相手は応じてくれましたか？", "会話が続きましたか？"]', datetime('now'));

-- レベル33
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(33, 'interact', '誰かと30分会話する', 'じっくり話そう', '["30分会話できましたか？", "深い話ができましたか？", "相手のことを知れましたか？"]', datetime('now')),
(33, 'interact', '友達に連絡する', 'メッセージでもいい', '["連絡できましたか？", "返事が来ましたか？", "嬉しかったですか？"]', datetime('now')),
(33, 'interact', '誰かに悩みを相談する', '小さな悩みでもいい', '["相談できましたか？", "聞いてもらえましたか？", "少し楽になりましたか？"]', datetime('now'));

-- レベル34
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(34, 'interact', '友達と会う約束をする', '会わなくてもいい、約束だけ', '["約束できましたか？", "日程を決められましたか？", "楽しみになりましたか？"]', datetime('now')),
(34, 'interact', '誰かと一緒にご飯を食べる', '外で食事しよう', '["一緒に食べられましたか？", "会話しながら食べられましたか？", "楽しかったですか？"]', datetime('now')),
(34, 'interact', 'グループでの会話に参加する', '聞くだけでもいい', '["参加できましたか？", "何か発言できましたか？", "疎外感を感じませんでしたか？"]', datetime('now'));

-- レベル35
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(35, 'interact', '友達と遊ぶ', '一緒に時間を過ごそう', '["遊べましたか？", "楽しかったですか？", "また会いたいと思いましたか？"]', datetime('now')),
(35, 'interact', '誰かに自分のことを話す', '最近の出来事を', '["話せましたか？", "聞いてもらえましたか？", "理解してもらえましたか？"]', datetime('now')),
(35, 'interact', '新しい人と知り合う', '名前を覚えよう', '["知り合えましたか？", "名前を覚えられましたか？", "また話したいと思いましたか？"]', datetime('now'));

-- ====================
-- レベル36〜42: 体を動かす
-- ====================

-- レベル36
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(36, 'exercise', '部屋でストレッチ10分', '体をほぐそう', '["ストレッチできましたか？", "10分続けられましたか？", "体がほぐれましたか？"]', datetime('now')),
(36, 'exercise', '家の階段を上り下りする', '5回でいい', '["上り下りできましたか？", "5回できましたか？", "息が上がりましたか？"]', datetime('now')),
(36, 'exercise', '外で散歩15分', 'ゆっくり歩こう', '["散歩できましたか？", "15分歩けましたか？", "気持ち良かったですか？"]', datetime('now'));

-- レベル37
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(37, 'exercise', '外で散歩30分', '少し長めに歩こう', '["30分歩けましたか？", "疲れすぎませんでしたか？", "景色を楽しめましたか？"]', datetime('now')),
(37, 'exercise', 'ラジオ体操をする', '全身を動かそう', '["ラジオ体操できましたか？", "最後までできましたか？", "体がスッキリしましたか？"]', datetime('now')),
(37, 'exercise', '公園で軽く体を動かす', '遊具を使ってもいい', '["公園に行けましたか？", "体を動かせましたか？", "楽しかったですか？"]', datetime('now'));

-- レベル38
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(38, 'exercise', '軽くジョギング10分', '走ってみよう', '["ジョギングできましたか？", "10分続けられましたか？", "気持ち良かったですか？"]', datetime('now')),
(38, 'exercise', '外で軽い筋トレ', '腕立てやスクワット', '["筋トレできましたか？", "何回できましたか？", "達成感がありましたか？"]', datetime('now')),
(38, 'exercise', '自転車に乗る', '20分くらい', '["自転車に乗れましたか？", "20分乗れましたか？", "風を感じられましたか？"]', datetime('now'));

-- レベル39
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(39, 'exercise', 'ジョギング30分', '長く走ってみよう', '["30分走れましたか？", "途中で休みましたか？", "完走できましたか？"]', datetime('now')),
(39, 'exercise', 'スポーツ施設を見に行く', 'ジムや体育館', '["見に行けましたか？", "中を見られましたか？", "通いたいと思いましたか？"]', datetime('now')),
(39, 'exercise', '縄跳びをする', '何回跳べるかな', '["縄跳びできましたか？", "何回跳べましたか？", "楽しかったですか？"]', datetime('now'));

-- レベル40
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(40, 'exercise', 'ジムの体験に行く', '初めてのジム', '["体験に行けましたか？", "マシンを使えましたか？", "また行きたいと思いましたか？"]', datetime('now')),
(40, 'exercise', 'ヨガをする', '動画を見ながらでもいい', '["ヨガできましたか？", "リラックスできましたか？", "体が柔らかくなりましたか？"]', datetime('now')),
(40, 'exercise', '1時間運動する', '何でもいい、体を動かそう', '["1時間運動できましたか？", "汗をかきましたか？", "爽快感がありましたか？"]', datetime('now'));

-- レベル41
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(41, 'exercise', '好きなスポーツを調べる', 'やってみたいことを探そう', '["調べられましたか？", "興味のあるスポーツが見つかりましたか？", "やってみたいと思いましたか？"]', datetime('now')),
(41, 'exercise', 'プールに行く', '泳がなくてもいい', '["プールに行けましたか？", "水に入れましたか？", "楽しかったですか？"]', datetime('now')),
(41, 'exercise', 'ダンス動画を見て踊る', '楽しく体を動かそう', '["踊れましたか？", "最後まで続けられましたか？", "楽しかったですか？"]', datetime('now'));

-- レベル42
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(42, 'exercise', 'スポーツ用品を買いに行く', 'シューズやウェア', '["買いに行けましたか？", "何か購入しましたか？", "運動が楽しみになりましたか？"]', datetime('now')),
(42, 'exercise', '誰かと一緒に運動する', '友達や家族と', '["一緒に運動できましたか？", "楽しかったですか？", "また一緒にやりたいと思いましたか？"]', datetime('now')),
(42, 'exercise', '運動を週間にする', '週3回を目標に', '["週3回運動できましたか？", "習慣になってきましたか？", "体調は良くなりましたか？"]', datetime('now'));

-- ====================
-- レベル43〜50: 新しいことに挑戦
-- ====================

-- レベル43
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(43, 'challenge', '興味のあることをリストアップ', 'やりたいことを書き出そう', '["リストアップできましたか？", "5つ以上書けましたか？", "ワクワクしましたか？"]', datetime('now')),
(43, 'challenge', 'オンライン講座を探す', '無料でもいい', '["探せましたか？", "興味のある講座が見つかりましたか？", "受けてみたいと思いましたか？"]', datetime('now')),
(43, 'challenge', '本屋で新しいジャンルの本を探す', 'いつもと違う棚へ', '["新しいジャンルを見ましたか？", "何か気になる本がありましたか？", "購入しましたか？"]', datetime('now'));

-- レベル44
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(44, 'challenge', '習い事の情報を集める', '体験できるところを探そう', '["情報を集められましたか？", "興味のある習い事が見つかりましたか？", "体験を申し込みたいと思いましたか？"]', datetime('now')),
(44, 'challenge', '新しい料理に挑戦する', 'レシピを見ながら', '["料理できましたか？", "美味しくできましたか？", "また作りたいと思いましたか？"]', datetime('now')),
(44, 'challenge', 'イベント情報をチェック', '行けそうなものを探そう', '["チェックできましたか？", "行きたいイベントが見つかりましたか？", "予定に入れましたか？"]', datetime('now'));

-- レベル45
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(45, 'challenge', '体験教室に申し込む', '一歩踏み出そう', '["申し込めましたか？", "日程を決められましたか？", "緊張しますか？"]', datetime('now')),
(45, 'challenge', 'ボランティアに参加する', '社会とつながろう', '["参加できましたか？", "役に立てましたか？", "やりがいを感じましたか？"]', datetime('now')),
(45, 'challenge', '新しいアプリを使ってみる', '学習アプリなど', '["使ってみましたか？", "続けられそうですか？", "役立ちそうですか？"]', datetime('now'));

-- レベル46
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(46, 'challenge', '体験教室に参加する', '新しい世界へ', '["参加できましたか？", "楽しかったですか？", "続けたいと思いましたか？"]', datetime('now')),
(46, 'challenge', 'コミュニティに参加する', 'サークルや集まり', '["参加できましたか？", "人と交流できましたか？", "また参加したいと思いましたか？"]', datetime('now')),
(46, 'challenge', '新しい場所に行く', '行ったことない街へ', '["行けましたか？", "何か発見がありましたか？", "楽しかったですか？"]', datetime('now'));

-- レベル47
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(47, 'challenge', '目標を立てる', '1ヶ月後の自分へ', '["目標を立てられましたか？", "達成可能な目標ですか？", "やる気が出ましたか？"]', datetime('now')),
(47, 'challenge', '新しいスキルを学び始める', '語学やプログラミングなど', '["学び始められましたか？", "楽しいと感じますか？", "続けられそうですか？"]', datetime('now')),
(47, 'challenge', '作品を作る', '絵や文章、何でもいい', '["作品を作れましたか？", "満足できましたか？", "誰かに見せたいと思いましたか？"]', datetime('now'));

-- レベル48
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(48, 'challenge', '誰かと約束をする', '1週間後に会う約束', '["約束できましたか？", "日時を決められましたか？", "楽しみですか？"]', datetime('now')),
(48, 'challenge', '将来の計画を立てる', '半年後、1年後', '["計画を立てられましたか？", "具体的に考えられましたか？", "前向きな気持ちになれましたか？"]', datetime('now')),
(48, 'challenge', 'チャレンジリストを作る', 'やりたいこと100個', '["リストを作れましたか？", "100個書けましたか？", "ワクワクしましたか？"]', datetime('now'));

-- レベル49
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(49, 'challenge', '約束を守る', '決めたことを実行しよう', '["約束を守れましたか？", "会えましたか？", "楽しかったですか？"]', datetime('now')),
(49, 'challenge', '新しい挑戦を始める', '本格的に始めよう', '["始められましたか？", "継続できそうですか？", "成長を感じますか？"]', datetime('now')),
(49, 'challenge', '誰かに感謝を伝える', '支えてくれた人へ', '["伝えられましたか？", "喜んでもらえましたか？", "温かい気持ちになれましたか？"]', datetime('now'));

-- レベル50
INSERT INTO task_templates (level, theme, title, message, reflection_questions, created_at) VALUES
(50, 'challenge', '50日間を振り返る', 'ここまで来たね', '["振り返れましたか？", "成長を感じますか？", "自分を誇りに思えますか？"]', datetime('now')),
(50, 'challenge', '次の目標を決める', 'これからも進もう', '["目標を決められましたか？", "やる気がありますか？", "未来が楽しみですか？"]', datetime('now')),
(50, 'challenge', '自分にご褒美をあげる', 'よく頑張ったね', '["ご褒美を決められましたか？", "自分を褒められましたか？", "幸せを感じますか？"]', datetime('now'));