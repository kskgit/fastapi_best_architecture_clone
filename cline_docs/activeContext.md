現在、ユーザーはfastapi及びこのプロジェクトのアーキテクチャを理解するために、TODO機能を追加しています。
TODO機能のデータモデルから作成を開始します。
開発は以下の順で進めます。
1. Define the database model (model)
2. Define data validation model (schema)
3. Defining Routes (router)
4. Writing a service
5. Writing database operations (crud)

TODO関連のファイルは`app/todo`配下にまとめる方針とします。
`backend/common/model.py`に`Todo`モデルが定義されていることを確認し、TODOテーブルを作成します。
