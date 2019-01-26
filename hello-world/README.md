# Hello World!

このDockerfileによって作成されたイメージを使うと、Hello Worldを2つの方法で表示できます。
また、本リポジトリは以下のファイルによって構成されています。

```
.
├── cmd
│   ├── hello
│   │   └── main.go
│   └── hello-server
│       └── main.go
├── Dockerfile
└── README.md
```

## ビルド方法

```bash
$ docker build -t hello-world:v1 .
```

## 使い方

### Hello World!コマンド

```bash
$ docker run --rm hello-world:v1
Hello World!
```

### Hello World!サーバ

```bash
$ docker run --rm -dp 8080:8080 hello-world:v1 /hello-server

$ curl localhost:8080
Hello World!
```
