#include "Labyrinth.h"

Labyrinth::Labyrinth()
{
	env[M][N] = {0};
	// Read File
	std::ifstream file;
	file.open ("input.txt", std::ifstream::in);

	if (!file.is_open()) {
		cout << "Error: Failed to open file.";
	}

	for (int i=0; i != M; ++i) {
		for (int j=0; j != N; ++j) {
			file >> env[i][j];
		}
	}

	memset(visited, 0, sizeof visited);
	memset(envclean, 0, sizeof envclean);

	bruteForceSearch();

	Node pointA = make_pair(ptA.first, ptA.second);
	Node pointB = make_pair(ptB.first, ptB.second);

	isPath = finRoute(pointB, pointA);

	writeOutput();
}

Labyrinth::~Labyrinth()
{
}

bool Labyrinth::isSafe(char mat[M][N], int visited[M][N], int i, int j, int x, int y)
{
	if (mat[x][y] == '#' || mat[i][j] == '#' || visited[x][y])
		return false;
	return true;
}

// Check the array position is inside the boundaries
bool Labyrinth::isValid(int x, int y)
{
	return (x < M && y < N && x >= 0 && y >= 0);
}

// Check the array position is inside the boundaries
bool Labyrinth::isValid(vector<Node> path, Node pt)
{
	return ((pt.first >= 0) && (pt.first < N) &&
		(pt.second >= 0) && (pt.second < N) &&
		(std::find(path.begin(), path.end(), pt) == path.end()));
}

// Find the Largest pathway
void Labyrinth::findLargestPathway(char mat[M][N], int visited[M][N], int i, int j, int x, int y, int& maxdist, int dist)
{
	// Update Max Distance
	if (i == x && j == y)
	{
		if (dist > maxdist)
			maxdist = dist;

		envclean[i][j] = 1;
		return;
	}

	// set (i, j) cell as visited
	visited[i][j] = 1;

	// go to bottom cell
	bool goToNext = 0;
	int k;
	for (k = 3; k >= 0; k--)
	{
		if (isValid(i + row[k], j + col[k]) && isSafe(mat, visited, i, j, i + row[k], j + col[k]))
		{
			envclean[i][j] = 1;
			goToNext = 1;
			break;
		}
	}
	if (goToNext)
		findLargestPathway(mat, visited, i + row[k], j + col[k], x, y, maxdist, dist + 1);

	// Backtrack - Remove (i, j) from visited matrix
	visited[i][j] = 0;
}

// Find route in a matrix mat from source cell (0, 0) to
// destination cell (N-1, N-1)
bool Labyrinth::finRoute(Node &curr, Node &dest)
{
	// include current cell in the path
	pathCell.push_back(curr);

	// if destination is found, return true
	if (curr.first == dest.first && curr.second == dest.second)
		return true;

	// Value of current position
	int n = envclean[curr.first][curr.second];

	// Evaluate all possible directions from current cell and recurse for each valid movement
	for (int i = 0; i < 4; i++)
	{
		// get next position using value of current cell
		int x = curr.first + row[i] * n;
		int y = curr.second + col[i] * n;

		Node next = make_pair(x, y);

		// Verify if it is possible to to next position from current position
		if (isValid(pathCell, next) && finRoute(next, dest))
			return true;
	}

	// Backtrack - exclude current cell from the path
	pathCell.pop_back();
	return false;
}


void Labyrinth::pathOut(vector<Node> path)
{
	int out[M][N] = { 0 };
	memset(out, 0, sizeof path);
	int i = 0;
	for (int i = 0; i < 10; i++)
	{
		out[path[i].first][path[i].second] = i;
	}

	for (int i = 0; i != M; ++i) {
		for (int j = 0; j != N; ++j) {
			std::cout << out[i][j];
		}
		std::cout << endl;
	}
	std::cout << endl;
}


// Brute - force search for the Largest Pathway
void Labyrinth::bruteForceSearch()
{
	for (int rowi = 0; rowi < M; rowi++)
	{
		for (int coli = 0; coli < N; coli++)
		{
			for (int rowf = 0; rowf < M; rowf++)
			{
				for (int colf = 0; colf < N; colf++)
				{
					int maxdist = 0;
					findLargestPathway(env, visited, rowi, coli, rowf, colf, maxdist, 0);
					if (maxdist >= max_dist)
					{
						ptA.first = rowi;
						ptA.second = coli;
						ptB.first = rowf;
						ptB.second = colf;
						max_dist = maxdist;
					}
				}
			}
		}
	}
	int maxdist = 0;
	clearEnv();
	findLargestPathway(env, visited, ptA.first, ptA.second, ptB.first, ptB.second, maxdist, 0);
}

void Labyrinth::clearEnv()
{
	for (int i = 0; i != M; ++i) {
		for (int j = 0; j != N; ++j) {
			envclean[i][j] = 0;
		}
	}
}
void Labyrinth::coutPath()
{
	cout << endl << "Pathway with ones and zeros" << endl;
	for (int i = 0; i != M; ++i) {
		for (int j = 0; j != N; ++j) {
			std::cout << envclean[i][j];
		}
		std::cout << endl;
	}
	std::cout << endl;
}

void Labyrinth::coutPathSorted()
{

	int out[M][N] = { 0 };
	memset(out, 0, sizeof pathCell);
	int i = 0;
	for (int i = 0; i < pathCell.size(); i++)
	{
		out[pathCell[i].first][pathCell[i].second] = i;
	}

	cout << endl << "Output:" << endl << max_dist+1 << endl;
	for (int i = 0; i != M; ++i) {
		for (int j = 0; j != N; ++j) {
			if (envclean[i][j])
				std::cout << out[i][j];
			else
				std::cout << env[i][j];
		}
		std::cout << endl;
	}
	std::cout << endl;
}

void Labyrinth::coutEnv()
{
	std::cout << endl << "Input:" << endl;
	for (int i = 0; i != M; ++i) {
		for (int j = 0; j != N; ++j) {
			std::cout << env[i][j];
		}
		std::cout << endl;
	}
	std::cout << endl;
}

void Labyrinth::writeOutput()
{
	int out[M][N] = { 0 };
	memset(out, 0, sizeof pathCell);
	int i = 0;
	for (int i = 0; i < pathCell.size(); i++)
	{
		out[pathCell[i].first][pathCell[i].second] = i;
	}

	ofstream outputFile ("output.txt");
	if (outputFile.is_open())
	{
		outputFile << "output\n" << max_dist << endl;
		for (int i = 0; i != M; ++i)
		{
			for (int j = 0; j != N; ++j)
			{
				if (envclean[i][j])
					outputFile << out[i][j];
				else
					outputFile << env[i][j];
			}
			outputFile << endl;
		}
	}
	outputFile.close();
}
