---
layout: post
title: Lucene学习笔记之一：简介和示例
categories: 技术
tags: [lucene,nlp]
keywords: lucene,nlp
date: 2016-03-21
permalink: Lucene-1-Setup-Mac
---
### Lucene简介 ###
[Lucene](http://lucene.apache.org)是一个开源的全文检索引擎工具包，提供了一个简单却强大的接口，是最受欢迎的全文索引和搜索的框架。

对于初学者，开始它真的只需要不到10分钟的时间。
<!--more-->

#### Lucene示例 ####
#### Maven依赖 ####
```
<properties>
...
<lucene.version>5.5.0</lucene.version>
</properties>

<dependency>
  <groupId>org.apache.lucene</groupId>
  <artifactId>lucene-core</artifactId>
  <version>${lucene.version}</version>
</dependency>
<dependency>
  <groupId>org.apache.lucene</groupId>
  <artifactId>lucene-analyzers-common</artifactId>
  <version>${lucene.version}</version>
</dependency>
<dependency>
  <groupId>org.apache.lucene</groupId>
  <artifactId>lucene-queryparser</artifactId>
  <version>${lucene.version}</version>
</dependency>
```

#### 应用常量 ####
```
public class Constants {

    public static final String QUESTION = "question";

    public static final String ANSWER = "answer";

    public static final String TAG = "tag";

    public static final String INDEX_PATH = "resources/test/index";

    public static final int HITS_PER_PAGE = 10;

}

```
#### Lucene创建索引 ####
多次运行会以append的形式加入到索引中。
```
public class LuceneIndexGenerator {

    public static void generate(@NonNull final String indexPath) throws IOException {
        final StandardAnalyzer analyzer = new StandardAnalyzer();
        final IndexWriterConfig config = new IndexWriterConfig(analyzer);

        IndexWriter writer = null;
        final Directory index = FSDirectory.open(Paths.get(indexPath));
        writer = new IndexWriter(index, config);
        addDoc(writer, "who am i?", "dongyuxi", "me");
        addDoc(writer, "who are you?", "you", "you");
        addDoc(writer, "who is it?", "nobody", "no");
        writer.close();
    }

    private static void addDoc(@NonNull final IndexWriter writer, @NonNull final String question, @NonNull final String answer,
            @NonNull final String tag) throws IOException {
        Document doc = new Document();
        doc.add(new TextField(Constants.QUESTION, question, Field.Store.YES));
        doc.add(new TextField(Constants.ANSWER, answer, Field.Store.YES));
        doc.add(new TextField(Constants.TAG, tag, Field.Store.YES));
        writer.addDocument(doc);
    }

    public static void main(String[] args) throws IOException {
        LuceneIndexGenerator.generate(Constants.INDEX_PATH);
    }

}
```

#### Lucene搜索 ####
```
public class LuceneQuerySearcher {

    private QueryParser queryParser;
    private IndexReader reader;
    private IndexSearcher searcher;

    public LuceneQuerySearcher(@NonNull final String indexPath) throws IOException {
        final StandardAnalyzer analyzer = new StandardAnalyzer();
        this.queryParser = new QueryParser(BaiduZhidaoConstants.QUESTION, analyzer);
        final Directory index = FSDirectory.open(Paths.get(indexPath));
        this.reader = DirectoryReader.open(index);
        this.searcher = new IndexSearcher(reader);
    }

    public void search(@NonNull final String queryString, final int hitsPerPage) throws ParseException, IOException {
        final Query query = queryParser.parse(queryString);
        final TopScoreDocCollector collector = TopScoreDocCollector.create(hitsPerPage);
        this.searcher.search(query, collector);
        final ScoreDoc[] docs = collector.topDocs().scoreDocs;

        if (docs == null) {
            System.out.println("find no docs for query" + queryString);
            return;
        }

        System.out.println("find " + docs.length + " docs for query " + queryString);
        for (int i = 0; i < docs.length; ++i) {
            final Document doc = this.searcher.doc(docs[i].doc);
            final String question = doc.get(Constants.QUESTION);
            final String answer = doc.get(Constants.ANSWER);
            final String tag = doc.get(Constants.TAG);
            System.out.println("-->record " + i + " question: [" + question + "] answer: [" + answer + "] tag: [" + tag + "]");
        }

    }

    public void close() throws IOException {
        this.reader.close();
    }

    public static void main(String[] args) throws IOException, ParseException {
        final LuceneQuerySearcher searcher = new LuceneQuerySearcher(Constants.INDEX_PATH);
        searcher.search("who", BaiduZhidaoConstants.HITS_PER_PAGE);
        searcher.close();
    }

}
```
