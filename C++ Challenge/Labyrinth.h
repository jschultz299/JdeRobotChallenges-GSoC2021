#pragma once

#include <iostream>
#include <fstream>
#include <string.h>
#include <cstring>

#include <cassert>
#include <algorithm>

#include <cstdlib>
#include <vector>

using namespace std;

// Input Dimension
#define M 5
#define N 7

// Coordinates of the pathway
typedef std::pair<int, int> Node;

// Array with possible directions
int const row[] = { -1, 0, 0, 1 };
int const col[] = { 0, -1, 1, 0 };

class Labyrinth
{
public:
	char env[M][N];
	Labyrinth();
	~Labyrinth();

public:
	bool isPath;
	void coutEnv();
	void coutPath();
	void coutPathSorted();

private:
	int visited[M][N], envclean[M][N];
	Node ptA, ptB;
	vector<Node> pathCell;
	int max_dist;

	bool isSafe(char mat[M][N], int visited[M][N], int i, int j, int x, int y);
	bool isValid(int x, int y);
	bool isValid(vector<Node> path, Node pt);

	void findLargestPathway(char mat[M][N], int visited[M][N], int i, int j, int x, int y, int& maxdist, int dist);
	bool finRoute(Node &curr, Node &dest);
	void pathOut(vector<Node> path);

	void bruteForceSearch();
	void clearEnv();

	void writeOutput();
};
